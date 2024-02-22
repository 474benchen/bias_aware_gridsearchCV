from sklearn.model_selection import KFold, StratifiedKFold, ParameterGrid
from sklearn.metrics import accuracy_score
from sklearn.base import clone
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from util import calculate_disparate_impact, calculate_statistical_parity_difference
from joblib import Parallel, delayed


class BiasAwareGridSearchCV:
    def __init__(self, estimator, param_grid, df, outcome_column, protected_attribute, privileged_value, unprivileged_value, favorable_result, cv=5, n_jobs=1, verbose=True):
        """
        Initializes the BiasAwareGridSearchCV object.

        Args:
            estimator: The machine learning estimator to use.
            param_grid: Dictionary with parameters names as keys and lists of parameter settings to try as values.
            df: DataFrame containing the training data.
            outcome_column: Name of the target column in df.
            protected_attribute: Name of the column representing the protected attribute.
            privileged_value: The value in the protected attribute column that represents the privileged group.
            unprivileged_value: The value in the protected attribute column that represents the unprivileged group.
            cv: Number of folds to use for cross-validation.
        """
        self.estimator = estimator
        self.param_grid = param_grid
        self.df = df
        self.outcome_column = outcome_column
        self.protected_attribute = protected_attribute
        self.privileged_value = privileged_value
        self.unprivileged_value = unprivileged_value
        self.favorable_result = favorable_result
        self.cv = cv
        self.n_jobs = n_jobs
        self.verbose = verbose
        self.results_ = []

    def fit(self, X, y, bias_function):
        """
        Runs the grid search with cross-validation over the specified parameter grid,
        evaluating models for accuracy and bias in parallel.

        Args:
            X_train: DataFrame containing the features from the training data.
            y_train: Series or array-like containing the target variable from the training data.
            bias_function: function to calculate the bias metric of interest.
        """
        kf = StratifiedKFold(n_splits=self.cv)

        def process_params(params):
            if self.verbose:
                print(f"Processing parameters: {params}")

            accuracies = []
            biases = []

            for train_index, val_index in kf.split(X, y):
                X_train_fold, X_val_fold = X.iloc[train_index], X.iloc[val_index]
                y_train_fold, y_val_fold = y.iloc[train_index], y.iloc[val_index]

                model = clone(self.estimator)
                model.set_params(**params)
                model.fit(X_train_fold, y_train_fold)
                preds = model.predict(X_val_fold)

                accuracy = accuracy_score(y_val_fold, preds)
                accuracies.append(accuracy)

                # Extract protected attribute for bias calculation
                protected_attr_val = X_val_fold[self.protected_attribute]
                temp_df = pd.DataFrame({self.outcome_column: y_val_fold, self.protected_attribute: protected_attr_val})
                temp_df[self.outcome_column + '_pred'] = preds
                bias = bias_function(temp_df, self.outcome_column + '_pred', self.protected_attribute, self.privileged_value, self.unprivileged_value, self.favorable_result)
                biases.append(bias)

            return {
                'params': params,
                'accuracy': np.mean(accuracies),
                'bias': np.mean(biases),
                'raw_biases': biases
            }

        self.results_ = Parallel(n_jobs=self.n_jobs)(
            delayed(process_params)(params) for params in ParameterGrid(self.param_grid)
        )


    def select_highest_accuracy_model(self):
        """
        Selects and retrains the model with the highest accuracy from the grid search results.

        Returns:
            The model with the highest accuracy.
        """
        best_params = max(self.results_, key=lambda x: x['accuracy'])['params']
        best_model = [model for model in self.results_ if model['params'] == best_params][0]

        if self.verbose:
            print(f"Selected model parameters: {best_params} with accuracy: {best_model['accuracy']}, bias: {best_model['bias']}")

        return self._retrain_model(best_params)

    def select_least_biased_model(self):
        """
        Selects and retrains the model with the least bias from the grid search results.

        Returns:
            The model with the least bias.
        """
        best_params = min(self.results_, key=lambda x: np.abs(x['bias']))['params']
        best_model = [model for model in self.results_ if model['params'] == best_params][0]

        if self.verbose:
            print(f"Selected model parameters: {best_params} with accuracy: {best_model['accuracy']}, bias: {best_model['bias']}")

        return self._retrain_model(best_params)

    def select_balanced_model(self, threshold):
        """
        Selects and retrains the model with the least bias among the top 'threshold' models with the highest accuracy.

        Args:
            threshold: The number of top models to consider based on accuracy.
        Returns:
            The model with the least bias among the top models based on accuracy.
        """
        top_accurate_models = sorted(self.results_, key=lambda x: x['accuracy'], reverse=True)[:threshold]
        best_params = min(top_accurate_models, key=lambda x: np.abs(x['bias']))['params']
        best_model = [model for model in self.results_ if model['params'] == best_params][0]

        if self.verbose:
            print(f"Selected model parameters: {best_params} with accuracy: {best_model['accuracy']}, bias: {best_model['bias']}")
            
        return self._retrain_model(best_params)

    def _retrain_model(self, params):
        """
        Retrains the model using the given parameters on the full dataset.

        Args:
            params: The parameters to use for the model.
        Returns:
            The retrained model.
        """
        model = clone(self.estimator)
        model.set_params(**params)
        model.fit(self.df.drop(columns=[self.outcome_column]), self.df[self.outcome_column])
        return model

    def find_optimum_model(self, margin):
        """
        Searches for the model with the least bias exhibited within the specified margin of distance
        from the highest accuracy.

        Args:
            margin: Float representing the tolerance in accuracy discrepancy
        Returns:
            The retrained model.
        """
        # Find the highest accuracy
        max_accuracy = max(result['accuracy'] for result in self.results_)

        # Filter models within the specified margin of the highest accuracy
        eligible_models = [result for result in self.results_ if result['accuracy'] >= max_accuracy - margin]

        if not eligible_models:
            raise ValueError("No models found within the specified accuracy margin.")

        # Select the model with the least bias among these
        best_model = min(eligible_models, key=lambda x: np.abs(x['bias']))

        if self.verbose:
            print(f"Selected model parameters: {best_model['params']} with accuracy: {best_model['accuracy']}, bias: {best_model['bias']}")

        # Retrain the model with the selected parameters
        return self._retrain_model(best_model['params'])
    
    def plot_accuracy(self, threshold):
        """
        Plots the line graph of models' accuracy and bias. X axis is accuracy. Y axis is bias.

        Args:
            threshold: The integer of top models to consider based on accuracy, draws line on the plot.
        Returns:
            The plot.
        """
        # Sorts models from lowest to highest accuracy
        sorted_models = sorted(self.results_, key=lambda x: x['accuracy'], reverse=True)
        
        # Get accuracy and bias
        plot_df = pd.DataFrame()
        plot_df['accuracy'] = [result['accuracy'] for result in sorted_models]
        plot_df['bias'] = [result['bias'] for result in sorted_models]

        # Find threshold value
        val = (plot_df.accuracy.loc[threshold - 1] + plot_df.accuracy.loc[threshold]) / 2

        # Plot accuracy and bias
        ax = sns.lmplot(plot_df, x='accuracy', y='bias')
        plt.axvline(x = val, color = 'r')
        return ax
    
    def plot_params(self, parameter):
        """
        Plots the line graph of parameters and bias, ideally for a continuous parameter. X axis is parameter. Y axis is bias.

        Args:
            paramenter (str): The name of a parameter from the initial param_grid. 
        Returns:
            The plot.
        """
        # Get parameter and bias
        plot_df = pd.DataFrame()
        plot_df[parameter] = [result['params'][parameter] for result in self.results_]
        plot_df['bias'] = [result['bias'] for result in self.results_]

        # Plot parameter and bias
        return sns.lmplot(plot_df, x=parameter, y='bias')

