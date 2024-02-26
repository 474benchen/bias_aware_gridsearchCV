---
layout: default
title: Home
nav_order: 1
---

# BAGS: Bias Aware Gridsearch(CV)
{: .fs-9 }

An exploratory venture into including bias considerations into the classical machine learning pipeline.
{: .fs-6 .fw-300 }

[Get started now][getting started]{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View it on GitHub][bags repo]{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Check out our Paper][bags paper]{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }

---

{: .note } 
Specific use cases and detailed examples can be found in the repo.


Welcome to the documentation for BiasAwareGridSearchCV. This tool is a practical extension for machine learning models, focusing on fairness during the hyperparameter tuning process.

BiasAwareGridSearchCV evaluates models based on both their accuracy and how fairly they treat a specified protected attribute, like age or gender. It offers different selection methods to find the most accurate, least biased, or a balanced model based on your needs. This approach is particularly useful in scenarios where decision fairness is as important as decision accuracy.


The tool also includes visualization features to help you understand the trade-offs between accuracy and bias in your models. With these, you can see how changes in parameters affect your model's fairness. Our documentation aims to make it easy to use BiasAwareGridSearchCV in your own machine learning workflows, helping you create models that are both effective and fair.

## Data

In development of this tool, we analyzed 4 different datasets available under public domain, each highlighting a different example of ways bias can present itself. The datasets analyzed are as follows:
  - Finance (UCI Adult Income Dataset)
  - Health (CDC Diabetes Diagnosis Data)
  - Recidivism (COMPAS Scores)
  - Mortgage Origination (Home Mortgage Disclosure Act Data)

## Methodology
### Preprocessing
Each dataset was individually cleaned, processed, and explored based on the focus of that dataset’s domain. In order to prepare for use with our grid search, each dataset needed to contain both a target variable and a protected attribute, which is the feature that is being evaluated for bias. 

### Development
For the purposes of our project, we decided to focus on RandomForest models, using either [statistical parity](https://474benchen.github.io/bias_aware_gridsearchCV/documentation/bias_functions/statistical_parity) or [disparate impact](https://474benchen.github.io/bias_aware_gridsearchCV/documentation/bias_functions/disparate_impact) as the bias metric. The basis of our tool is heavily modeled after sklearn’s GridSearchCV. We modified it by adding in a bias evaluation layer, where one would be able to select models using varied criteria. Our method allows the selection of the least biased model, most accurate model, or most balanced model. 

// Insert graphic depicting which was the protected attribute and target variable for each dataset, and the selected bias metric


[bags repo]: https://github.com/474benchen/bias_aware_gridsearchCV/tree/main
[bags paper]: https://www.google.com/
[getting started]: https://474benchen.github.io/bias_aware_gridsearchCV/getting_started/
