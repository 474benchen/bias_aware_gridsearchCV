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


BiasAwareGridSearchCV is a Python tool created to address a critical need in machine learning: reducing bias. Developed as an extension of scikit-learn, this package helps data professionals build fairer machine learning models by integrating bias into the classical machine learning workflow. It’s designed for situations where decisions could be influenced by factors like gender or race, and where it’s crucial to ensure these decisions are as unbiased as possible.

Our tool stands out by not only measuring model performance in terms of accuracy but also considering how fair a model is. With BiasAwareGridSearchCV, you can evaluate and select models based on both their accuracy and their level of exhibited bias as well as visualize features for a clearer understanding of the trade-offs between bias and accuracy.

## Overview

![](../../assets/images/ml_flowchart.png)

"[Wroclaw University Library digitizing rare archival texts](https://www.flickr.com/photos/97810305@N08/9401451269)" by [j_cadmus](https://www.flickr.com/photos/97810305@N08) is marked with [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/?ref=openverse).

<!-- <img align="left" src="/docs/assets/images/ml_flowchart.png" alt="ML process flowchart" width="30%" height="60%"> -->

The package is user-friendly and fits smoothly into standard machine learning workflows. The figure shows a simplified view of the machine learning process. 

Our algorithm is created to be used during the “Hyperparameter Tuning” stage, where the selected model is trained using various parameters and evaluated. Our tool inserts bias consideration into this step by making it a factor in model evaluation alongside traditional performance metrics.

In short, BiasAwareGridSearchCV is our effort to ensure that AI and machine learning contribute positively and fairly to our society, providing tools that help mitigate bias in automated decision-making.


<br>
<br>
<br>

{: .note } 
This work runs adjacent to existing bias mitigation techniques - it is presented as a novel step to the pre-processing, in-processing, and post-processing steps that already exist.

<br>

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
