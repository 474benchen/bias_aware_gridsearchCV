import pandas as pd

def calculate_disparate_impact(df, outcome_column, privileged_groups, unprivileged_groups):
    """
    Calculates the disparate impact ratio comparing privileged vs unprivileged groups.

    Disparate impact is calculated as the ratio of the probability of a favorable outcome 
    for the unprivileged group to that for the privileged group. A value of 1 indicates fairness, 
    values less than 1 indicate less favorable outcomes for the unprivileged group, and values greater 
    than 1 indicate less favorable outcomes for the privileged group.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        outcome_column (str): Name of the column with the binary outcome (1 for positive outcome, 0 for negative).
        privileged_groups (dict): Dictionary with protected attributes as keys and privileged values as values.
        unprivileged_groups (dict): Dictionary with protected attributes as keys and unprivileged values as values.
    Returns:
        float: The disparate impact ratio.
    """
    # Initialize variables to store probabilities
    prob_privileged, prob_unprivileged = 1, 1

    # Calculate probability of favorable outcome for privileged groups
    for attr, value in privileged_groups.items():
        prob_privileged *= df[(df[attr] == value) & (df[outcome_column] == 1)].shape[0] / df[df[attr] == value].shape[0]

    # Calculate probability of favorable outcome for unprivileged groups
    for attr, value in unprivileged_groups.items():
        prob_unprivileged *= df[(df[attr] == value) & (df[outcome_column] == 1)].shape[0] / df[df[attr] == value].shape[0]

    # Calculate disparate impact
    disparate_impact = prob_unprivileged / prob_privileged

    return disparate_impact