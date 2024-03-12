---
layout: default
title: Statistical Parity
parent: Bias Statistic Functions
grand_parent: Documentation
permalink: /documentation/bias_functions/statistical_parity
---

# Statistical Parity Difference
Calculates the statistical parity difference for a single protected attribute comparing privileged and unprivileged values.
{: .fs-6 .fw-300 }

```py
def calculate_statistical_parity_difference(df, outcome_column, protected_attribute, 
privileged_value, unprivileged_value, favorable_result)
```
## Parameters

- `df` (`pd.DataFrame`): The DataFrame containing the dataset. This should include the outcome column and the protected attribute.

- `outcome_column` (`str`): The name of the column in the DataFrame that represents the outcome of the prediction. The outcome should be binary, typically encoded as 1 for a favorable result and 0 for an unfavorable result.

- `protected_attribute` (`str`): The name of the column in the DataFrame that represents the protected attribute. This attribute is used to differentiate between the privileged and unprivileged groups (e.g., 'gender', 'race').

- `privileged_value` (`str` or `int`): The value within the protected attribute that represents the privileged group. For instance, if 'gender' is the protected attribute, 'male' might be designated as the privileged value.

- `unprivileged_value` (`str` or `int`): The value within the protected attribute that represents the unprivileged group. Using the same example, if 'gender' is the protected attribute, 'female' might be the unprivileged value.

- `favorable_result` (`int`): The value in the outcome column that is considered a favorable result. Typically, this is 1 for a positive outcome.

## Returns

- `float`: The statistical parity difference. A value of 0 implies fairness, a negative value indicates a bias against the unprivileged group, and a positive value indicates a bias in favor of the unprivileged group.


## Example 
This example demonstrates how to use the calculate_statistical_parity_difference function on a sample dataset. The dataset contains information on loan approvals, with 'gender' as the protected attribute.

```
>>> import pandas as pd
>>> from util import calculate_statistical_parity_difference
# Example dataset
>>> data = {
    'gender': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
    'loan_approved': [1, 0, 1, 1, 1, 1, 1, 0]
}
>>> df = pd.DataFrame(data)
>>> outcome_column = 'loan_approved'
>>> protected_attribute = 'gender'
>>> privileged_value = 'male'
>>> unprivileged_value = 'female'
>>> stat_parity_diff = calculate_statistical_parity_difference(df, outcome_column, \
protected_attribute, privileged_value, unprivileged_value, 1)
>>> print("Statistical Parity Difference:", stat_parity_diff)
Statistical Parity Difference: -0.5
```

The output indicates the degree of statistical parity difference in the loan approval process between males and females. A value close to 0 implies fairness, a negative value indicates bias in against the unprivileged group, and a positive value indicates bias in favor of the unprivileged group.

This result indicates a bias against the unprivileged group (in this case, 'female') in the context of loan approvals.
