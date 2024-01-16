import pandas as pd

def calculate_disparate_impact(df, outcome_column, protected_attribute, privileged_value, unprivileged_value):
    """
    Calculates the disparate impact ratio for a single protected attribute comparing privileged and unprivileged values.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        outcome_column (str): Name of the column with the binary outcome (1 for positive outcome, 0 for negative).
        protected_attribute (str): The protected attribute to consider (e.g., 'gender', 'race').
        privileged_value (str or int): The value of the protected attribute that represents the privileged group.
        unprivileged_value (str or int): The value of the protected attribute that represents the unprivileged group.
    Returns:
        float: The disparate impact ratio.
    """
    # Probability of favorable outcome for privileged group
    prob_privileged = df[(df[protected_attribute] == privileged_value) & (df[outcome_column] == 1)].shape[0] / df[df[protected_attribute] == privileged_value].shape[0]

    # Probability of favorable outcome for unprivileged group
    prob_unprivileged = df[(df[protected_attribute] == unprivileged_value) & (df[outcome_column] == 1)].shape[0] / df[df[protected_attribute] == unprivileged_value].shape[0]

    # Calculate disparate impact
    disparate_impact = prob_unprivileged / prob_privileged

    return disparate_impact

