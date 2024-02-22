---
layout: default
title: Home
nav_order: 1
---

# BAGS: Bias Aware Gridsearch(CV)
{: .fs-9 }

An exploratory venture into including bias considerations into the classical machine learning pipeline.
{: .fs-6 .fw-300 }

[Get started now](/getting_started/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View it on GitHub][bags repo]{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Check out our Paper][bags paper]{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }

---

{: .note } 
Specific use cases and detailed examples can be found in the repo.


Welcome to the documentation for BiasAwareGridSearchCV. This tool is a practical extension for machine learning models, focusing on fairness during the hyperparameter tuning process.

BiasAwareGridSearchCV evaluates models based on both their accuracy and how fairly they treat a specified protected attribute, like age or gender. It offers different selection methods to find the most accurate, least biased, or a balanced model based on your needs. This approach is particularly useful in scenarios where decision fairness is as important as decision accuracy.


The tool also includes visualization features to help you understand the trade-offs between accuracy and bias in your models. With these, you can see how changes in parameters affect your model's fairness. Our documentation aims to make it easy to use BiasAwareGridSearchCV in your own machine learning workflows, helping you create models that are both effective and fair.

[bags repo]: https://github.com/474benchen/bias_aware_gridsearchCV/tree/main
[bags paper]: https://www.google.com/
