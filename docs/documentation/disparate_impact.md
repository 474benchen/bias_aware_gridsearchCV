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
def calculate_disparate_impact(df, outcome_column, protected_attribute, privileged_value, unprivileged_value)
```

## Example 
This example demonstrates how to use the calculate_disparate_impact function on a sample dataset. The dataset contains information on loan approvals, with 'gender' as the protected attribute.

```
>>> import pandas as pd
>>> from util import calculate_disparate_impact
# Example dataset
>>> data = {
    'gender': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
    'loan_approved': [1, 0, 1, 1, 0, 1, 1, 0]
}
>>> df = pd.DataFrame(data)

>>> outcome_column = 'loan_approved'
>>> protected_attribute = 'gender'
>>> privileged_value = 'male'
>>> unprivileged_value = 'female'
>>> disparate_impact = calculate_disparate_impact(df, outcome_column, protected_attribute, privileged_value, unprivileged_value)
>>> print("Disparate Impact Ratio:", disparate_impact)
Disparate Impact Ratio: 0.25
```

The output indicates the degree of disparity in the loan approval process between males and females. A value close to 0 implies fairness, a negative value indicates bias in favor of the unprivileged group, and a positive value indicates bias against the unprivileged group.

With this output, we can see that there is a slight bias against the unprivileged group (in this case, 'female') in the context of loan approvals.
