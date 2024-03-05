---
layout: default
title: A Cautionary Tale
nav_order: 10
permalink: caution/
---

# Bias in Practice

Although it may be tempting to just look for bias and correct for it, there are many situations where this approach could be grossly erroneous.

'Fair-washing' refers to the practice of superficially addressing bias in machine learning models to give the appearance of fairness, without actually addressing underlying discriminatory patterns or ensuring equitable outcomes. Bias is a "grey-area" topic requiring domain knowledge and careful consideration to correct - Such approaches may inadvertently overlook or obscure the complexities and nuances unique to each situation, potentially perpetuating or even exacerbating unfairness.

While it may feel good to reduce bias, it's far more important to carefully consider the implications of your efforts.

## Example:

{: .note } 
This is a trivial example - real life situations are much more complex.

To illustrate how one must address bias responsibly and cautiously, lets consider the Titanic dataset. One protected attribute that is extremely common to encounter is gender. Income, healthcare, hiring, etc. are all domains that have historically been subject to considerable bias and unfairness in regards to a subject's gender. 
