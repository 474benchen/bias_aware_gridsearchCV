---
layout: default
title: Bias Aware Gridsearch CV
parent: Documentation
permalink: /documentation/bias_aware_gridsearch_cv
---

# Bias Aware Gridsearch CV (BAGS)

### `class BiasAwareGridSearchCV(estimator, param_grid, df, outcome_column, protected_attribute, privileged_value, unprivileged_value, favorable_result, cv=5, n_jobs=1, verbose=True)`


Bias Aware GridsearchCV is an extension of SciKitLearn's GridsearchCV, with additional consideration 
for a provided bias metric. 

## Parameters
- estimator (estimator object): The machine learning estimator to be used. This should be compatible with scikit-learn estimators.

- param_grid (dict): A dictionary containing parameter names as keys and lists of parameter settings to try as values.

- df (pd.DataFrame): The DataFrame containing the training data. This must include the target outcome column and the protected attribute.

- outcome_column (str): The name of the column in the DataFrame representing the target outcome, typically encoded as binary values.

- protected_attribute (str): The name of the column in the DataFrame representing the protected attribute, which could be any categorical feature (e.g., 'gender', 'race').

- privileged_value (str or int): The value in the protected attribute column indicating the privileged group, such as 'male' for a 'gender' attribute.

- unprivileged_value (str or int): The value in the protected attribute column indicating the unprivileged group, like 'female' in the case of a 'gender' attribute.

- favorable_result (int): The value in the outcome column that denotes a favorable result, often 1 for positive and 0 for negative outcomes.

- cv (int, default=5): The number of cross-validation folds.

- n_jobs (int, default=1): The number of jobs to run in parallel during the grid search.

- verbose (bool, default=True): Enables verbose output during the grid search if set to True.

## Attributes

- results_: list of dict of values with the structure:

| Key                         | Value                                                                   |
|--------------------------------|-----------------------------------------------------------------------------------------------------|
| `params (dict)`                          | Parameters used to initialize the model.                       |
| `accuracy (float)`| Average accuracy of the model across folds.                          |
| `bias (float)`    | Average exhibited bias across folds.                                |
| `raw_bias (list)`        | Exhibited bias for each fold.                          |

---

## Examples

```
>>> import pandas as pd
>>> import seaborn as sns
>>> from bias_aware_gridsearch import BiasAwareGridSearchCV
>>> from util import calculate_disparate_impact
>>> from sklearn.ensemble import RandomForestClassifier
# load in titanic data
>>> df = sns.load_dataset('titanic')
>>> df = df[['pclass', 'age', 'alone','sex', 'survived']]
# transform categorical to binary
>>> df['first_class'] = df['pclass'] == 1
>>> df = df[['first_class', 'age', 'alone', 'survived']].dropna()
>>> rfc = RandomForestClassifier()
>>> parameter_grid = {'n_estimators': [100, 200], 'max_depth': [5, 10]}
>>> clf = BiasAwareGridSearchCV(rfc, parameter_grid, df, 'survived', 'first_class', 1, 0, 1)
>>> clf.fit(df.drop(columns=['survived']), df['survived'], calculate_disparate_impact)
Processing parameters: {'max_depth': 5, 'n_estimators': 100}
Processing parameters: {'max_depth': 5, 'n_estimators': 200}
Processing parameters: {'max_depth': 10, 'n_estimators': 100}
Processing parameters: {'max_depth': 10, 'n_estimators': 200}
>>> best_model_acc = clf.select_highest_accuracy_model()
Selected model parameters: {'max_depth': 5, 'n_estimators': 100} with accuracy: 0.7087363340884467, bias: 0.8825532742303706
>>> best_model_bias = clf.select_least_biased_model()
Selected model parameters: {'max_depth': 10, 'n_estimators': 200} with accuracy: 0.6541416330148725, bias: 0.7175751435857917
>>> best_balanced_model = clf.select_balanced_model(threshold=3)
Selected model parameters: {'max_depth': 10, 'n_estimators': 100} with accuracy: 0.6582980399881808, bias: 0.7226774022458278
```

---

## Methods

| Method                         | Description                                                                                         |
|--------------------------------|-----------------------------------------------------------------------------------------------------|
| `fit(X, y, bias_function)`                          | Runs grid search with cross-validation, evaluating models for accuracy and bias.                                                                                                                                   |
| `select_highest_accuracy_model()`| Selects the model with the highest accuracy from the grid search results.                          |
| `select_least_biased_model()`    | Selects the model with the least bias from the grid search results.                                |
| `select_balanced_model()`        | Selects the model with the least bias among top models based on accuracy.                          |
| `find_optimum_model()`           | Searches for the model with least bias within a margin of highest accuracy.                        |
| `plot_accuracy(threshold)`                | Plots a line graph of models' accuracy and bias. Draws an additional line at the "threshold" best model                                                                                                                                   |
| `plot_params(parameter)`                  | Plots a line graph of a parameter against bias, ideal for a continuous parameter.         |

---

### `fit(X,y,bias_function)`

Run fit with all sets of parameters alongside a bias function.

#### Parameters

- X: `array-like` of shape (n_samples, n_features)
Training vector, where n_samples is the number of samples and n_features is the number of features.

- y: `array-like` of shape (n_samples, n_output)
Target relative to X for classification or regression.

- bias_function: `callable` -> bias calculator

Function to calculate a bias metric of interest. Criteria for the function are that 0 must represent
a fair value.

#### Returns

- `None` - populates the instance with the results derived from the provided parameter grid.

---

### `select_highest_accuracy_model()`

Selects and retrains the model with the highest accuracy based on the results of the grid search.

#### Returns

- **best_model**: `estimator` instance  
  The retrained model instance with the highest accuracy from the grid search results.

---

### `select_least_biased_model()`

Selects and retrains the model with the least bias based on the results of the grid search.

#### Returns

- **best_model**: `estimator` instance  
  The retrained model instance with the least bias from the grid search results.

---

### `select_balanced_model(threshold)`

Selects and retrains the model with the least bias among the top models with the highest accuracy.

#### Parameters

- **threshold**: `int`  
  The number of top models to consider based on accuracy.

#### Returns

- **best_model**: `estimator` instance  
  The retrained model with the least bias among the top models based on accuracy.

---

### `find_optimum_model(margin)`

Searches for and retrains the model with the least bias within a specified margin of the highest accuracy.

#### Parameters

- **margin**: `float`  
  The tolerance in accuracy discrepancy to consider when selecting the optimum model.

#### Returns

- **best_model**: `estimator` instance  
  The retrained model that exhibits the least bias within the specified margin of the highest accuracy.

#### Raises

- **ValueError**:  
  If no models are found within the specified accuracy margin.

---

### `plot_accuracy(threshold)`

Plots a line graph of models' accuracy and bias. The X-axis represents accuracy, and the Y-axis represents bias. A line is drawn on the plot to indicate the accuracy threshold.

#### Parameters

- **threshold**: `int`  
  The number of top models to consider based on accuracy. This value is used to draw a line on the plot.

#### Returns

- **ax**: `matplotlib.axes.Axes` instance  
  The plot object showing the relationship between accuracy and bias.

---

### `plot_params(parameter)`

Plots a line graph showing the relationship between a specified parameter and bias. The X-axis represents the parameter value, and the Y-axis represents bias.

#### Parameters

- **parameter**: `str`  
  The name of a parameter from the initial `param_grid`.

#### Returns

- **plot**: `matplotlib.axes.Axes` instance  
  The plot object showing the relationship between the specified parameter and bias.
