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

```
>>> import pandas as pd
>>> import seaborn as sns
>>> from util import calculate_disparate_impact
# load in titanic data
>>> df = sns.load_dataset('titanic')
>>> df['sex'] = df['sex']=='male'
>>> calculate_disparate_impact(df, 'survived', 'sex', 1, 0, 1)
-2.928037164728569
```

For our disparate impact ratio, a positive value implies a bias against the unprivileged group and a negative value implies a bias for the unprivileged group. A value of 0 implies a bias neutral state. From this result, we can see that there is an extremely severe degree of bias against the privileged group. That is, women were far more likely to survive titanic than men. Looks like we have a case on our hands, right? Large bias which can be easily corrected. Case closed.

While this could be a tempting conclusion, especially if it were a less trivial example, this obviously is not a case of bias we want to trifle with. This heavy bias is a result of real life intentions - when a ship first sinks, women and children are prioritized. On paper it may look like an issue to correct, but in reality this is an intended consequence and an arguably beneficial one. A more worthwhile venture in this case would be to consider bias in the context of ticket class - it would indicate a problematic bias if more first class passengers survived for example.

```
>>> import pandas as pd
>>> import seaborn as sns
>>> from util import calculate_disparate_impact
# load in titanic data
>>> df = sns.load_dataset('titanic')
>>> df['pclass'] = df['pclass'] == 1
>>> calculate_disparate_impact(df, 'survived', 'pclass', 1, 0, 1)
0.5152941176470589
```

From this result, we can see that there is a demonstrated bias in favor of first class passengers in terms of survival.

Some situations in real life will inherently be biased - this is just how the world works. Let's briefly consider another example, breast cancer. Women are far more likely to be predicted to have breast cancer by any medical model. Is this indicative of a gender based bias? Well, yes, but not an unfair one. [Women have a 13% chance of getting breast cancer](https://www.cancer.org/cancer/types/breast-cancer/about/how-common-is-breast-cancer.html#:~:text=Overall%2C%20the%20average%20risk%20of,will%20never%20have%20the%20disease.) while [men barely have a chance](https://www.cancer.org/cancer/types/breast-cancer-in-men/about/key-statistics.html#:~:text=For%20men%2C%20the%20average%20lifetime,risk%20factors%20for%20breast%20cancer.). In this case, it would be more alarming if a model produced on this data didn't demonstrate a disparate impact between genders.

No matter the context, it's critical to carefully consider the implications of your efforts. It's easy to search for bias to correct, but bias mitigation as a topic demands exhaustive domain knowledge to cautiously and comprehensively address.