---
layout: default
title: Home
nav_order: 1
---

# BAGS: Bias Aware Gridsearch(CV)
{: .fs-9 }

An exploratory venture into including bias considerations into the classical machine learning pipeline.
{: .fs-6 .fw-300 }

[Get started now](#getting-started){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View it on GitHub][bags repo]{: .btn .fs-5 .mb-4 .mb-md-0 }

---

{: .note } Specific use cases and detailed examples can be found in the repo.


Welcome to the documentation for BiasAwareGridSearchCV. This tool is a practical extension for machine learning models, focusing on fairness during the hyperparameter tuning process.

BiasAwareGridSearchCV evaluates models based on both their accuracy and how fairly they treat a specified protected attribute, like age or gender. It offers different selection methods to find the most accurate, least biased, or a balanced model based on your needs. This approach is particularly useful in scenarios where decision fairness is as important as decision accuracy.

The tool also includes visualization features to help you understand the trade-offs between accuracy and bias in your models. With these, you can see how changes in parameters affect your model's fairness. Our documentation aims to make it easy to use BiasAwareGridSearchCV in your own machine learning workflows, helping you create models that are both effective and fair.

## Getting started


To replicate our environment, you can choose from the following options. Regardless of which option,
in order to explore our work:

1. Clone the repository:

    ```
    git clone https://github.com/474benchen/biased_gridsearch.git
    ```

2. Navigate to the project directory:

    ```
    cd biased_gridsearch
    ```
### Option 1: Using requirements.txt

Ensure that you have pip installed before attempting this option. Instructions can be found [here](https://pip.pypa.io/en/stable/installation/).

1. Install the required packages using pip:

    ```
    pip install -r requirements.txt
    ```


### Option 2: Reconstructing the Conda Environment

Ensure that you have conda installed before attempting this option. Distributions can be found [here](https://www.anaconda.com/download).

1. Create a conda environment from the provided environment.yml file:

    ```
    conda env create -f environment.yml
    ```

2. Activate the conda environment:

    ```
    conda activate biased_gs
    ```

[source file for this page]: https://github.com/just-the-docs/just-the-docs/blob/main/index.md
[Template README]: https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md
[bags repo]: https://github.com/474benchen/bias_aware_gridsearchCV/tree/main