---
layout: default
title: Bias Aware Gridsearch CV
parent: documentation
permalink: /documentation/bias_aware_gridsearch_cv
---

# Bias Aware Gridsearch CV (BAGS)

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



## Methods

| Method                         | Description                                                                                         |
|--------------------------------|-----------------------------------------------------------------------------------------------------|
| `fit(x,y,bias_function)`                          | Runs grid search with cross-validation, evaluating models for accuracy and bias.                   |
| `select_highest_accuracy_model()`| Selects the model with the highest accuracy from the grid search results.              |
| `select_least_biased_model()`    | Selects the model with the least bias from the grid search results.                   |
| `select_balanced_model()`        | Selects the model with the least bias among top models based on accuracy.             |
| `find_optimum_model()`           | Searches for the model with least bias within a margin of highest accuracy.                        |
| `plot_accuracy(threshold)`                | Plots a line graph of models' accuracy and bias. Draws an additional line at the "threshold" best model                                                 |
| `plot_params(parameter)`                  | Plots a line graph of a parameter against bias, ideal for a continuous parameter.                  |
