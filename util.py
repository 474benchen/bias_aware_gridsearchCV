import pandas as pd
import pickle

def calculate_disparate_impact(df, outcome_column, protected_attribute, privileged_value, unprivileged_value, favorable_result):
    """
    Calculates the disparate impact ratio for a single protected attribute comparing privileged and unprivileged values.

    A value of 0 implies perfect fairness, a negative value implies a bias in favor of the unprivileged group,
    a positive value implies a bias against the unprivileged group.

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
    prob_privileged = df[(df[protected_attribute] == privileged_value) & (df[outcome_column] == favorable_result)].shape[0] / df[df[protected_attribute] == privileged_value].shape[0]

    # Probability of favorable outcome for unprivileged group
    prob_unprivileged = df[(df[protected_attribute] == unprivileged_value) & (df[outcome_column] == favorable_result)].shape[0] / df[df[protected_attribute] == unprivileged_value].shape[0]

    # Calculate disparate impact
    disparate_impact = prob_unprivileged / prob_privileged

    return 1 - disparate_impact

def calculate_statistical_parity_difference(df, outcome_column, protected_attribute, privileged_value, unprivileged_value, favorable_result):
    """ 
    Calculate statistical parity difference for pandas table that includes protected attribute and prediction. 

    A value of 0 implies perfect fairness, a negative value implies a bias against the unprivileged group,
    a positive value implies a bias for the unprivileged group.
    
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        outcome_column (str): Column name of prediction attribute in DataFrame
        protected_attribute (str): Column name of targeted attribute in DataFrame.
        privileged_value (str or int): The value of the protected attribute that represents the privileged group.
        unprivileged_value (str or int): The value of the protected attribute that represents the unprivileged group.
    Returns:
        float: Statistical parity difference.
    """
    # Probability of a positive outcome for the unprivileged group
    prob_unprivileged = (df[df[protected_attribute] == unprivileged_value][outcome_column] == favorable_result).mean()
    # Probability of a positive outcome for the privileged group
    prob_privileged = (df[df[protected_attribute] == privileged_value][outcome_column] == favorable_result).mean()
    # Calculate statistical parity difference
    return prob_unprivileged - prob_privileged

def save_model(model, filepath):
    """
    Helper function to save a model after training. Filepath should end in 'pkl'
    for pickle format.

    Args:
        model (sklearn model): trained model to be saved
        filepath (string): filename or path to file for model to be saved
    """
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
