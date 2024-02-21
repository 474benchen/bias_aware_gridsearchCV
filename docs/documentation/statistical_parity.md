---
layout: default
title: statistical parity
parent: bias statistic functions
grand_parent: documentation
permalink: /documentation/bias_functions/statistical_parity
---

# Statistical Parity Difference
Calculates the statistical parity difference for a single protected attribute comparing privileged and unprivileged values.
{: .fs-6 .fw-300 }

```py
def calculate_statistical_parity_difference(df, outcome_column, protected_attribute, privileged_value, unprivileged_value)
```

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
>>> stat_parity_diff = calculate_statistical_parity_difference(df, outcome_column, protected_attribute, privileged_value, unprivileged_value)
>>> print("Statistical Parity Difference:", stat_parity_diff)
Statistical Parity Difference: -0.5
```

The output indicates the degree of statistical parity difference in the loan approval process between males and females. A value close to 0 implies fairness, a negative value indicates bias in against the unprivileged group, and a positive value indicates bias in favor of the unprivileged group.

This result indicates a bias against the unprivileged group (in this case, 'female') in the context of loan approvals.