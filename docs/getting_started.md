---
layout: default
title: Getting Started
nav_order: 3
permalink: getting_started/
---

# Getting Started


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

## Option 1: Reconstructing the Conda Environment (recommended)

Ensure that you have conda installed before attempting this option. Distributions can be found [here](https://www.anaconda.com/download).

1. Create a conda environment from the provided environment.yml file:

    ```
    conda env create -f environment.yml
    ```

2. Activate the conda environment:

    ```
    conda activate biased_gs
    ```

## Option 2: Using requirements.txt

Ensure that you have pip installed before attempting this option. Instructions can be found [here](https://pip.pypa.io/en/stable/installation/).

1. Install the required packages using pip:

    ```
    pip install -r requirements.txt
    ```
