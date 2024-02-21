---
layout: default
title: disparate impact
parent: bias statistic functions
grand_parent: documentation
permalink: /documentation/bias_functions/disparate_impact
---

# Disparate Impact
Calculates the disparate impact ratio for a single protected attribute comparing privileged and unprivileged values.
{: .fs-6 .fw-300 }

```py
def calculate_disparate_impact(df, outcome_column, protected_attribute, 
privileged_value, unprivileged_value, favorable_result)
```

## Parameters

- `df` (`pd.DataFrame`): The DataFrame containing the data. This should include both the outcome column and the protected attribute.

- `outcome_column` (`str`): The name of the column in the DataFrame that represents the binary outcome. The outcomes should be encoded as 1 for a positive outcome and 0 for a negative outcome.

- `protected_attribute` (`str`): The name of the column in the DataFrame that represents the protected attribute. This could be any categorical attribute for which fairness is to be assessed (e.g., 'gender', 'race').

- `privileged_value` (`str` or `int`): The value in the protected attribute column that represents the privileged group. For example, if the protected attribute is 'gender', the privileged value could be 'male'.

- `unprivileged_value` (`str` or `int`): The value in the protected attribute column that represents the unprivileged group. Following the earlier example, this could be 'female' if the protected attribute is 'gender'.

- `favorable_result` (`int`): The value in the outcome column that represents a favorable result. Typically, this is 1 for a positive outcome and 0 for a negative outcome.

## Returns

- `float`: The disparate impact ratio. A value of 0 implies perfect fairness, a negative value indicates a bias in favor of the unprivileged group, and a positive value indicates a bias against the unprivileged group.


## Example 
This example demonstrates how to use the calculate_disparate_impact function on a sample dataset. The dataset contains information on loan approvals, with 'gender' as the protected attribute.

```
>>> import pandas as pd
>>> from util import calculate_disparate_impact
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
>>> disparate_impact = calculate_disparate_impact(df, outcome_column, \
protected_attribute, privileged_value, unprivileged_value, 1)
>>> print("Disparate Impact Ratio:", disparate_impact)
Disparate Impact Ratio: 0.5
```

The output indicates the degree of disparity in the loan approval process between males and females. A value close to 0 implies fairness, a negative value indicates bias in favor of the unprivileged group, and a positive value indicates bias against the unprivileged group.

With this output, we can see that there is a bias against the unprivileged group (in this case, 'female') in the context of loan approvals.
