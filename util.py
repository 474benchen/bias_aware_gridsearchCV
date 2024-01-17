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

def calculate_disparate_impact_dict(df, outcome_column, protected_attribute):
    """
    Calculates the disparate impact ratio for a single protected attribute comparing privileged and unprivileged values.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        outcome_column (str): Name of the column with the binary outcome (1 for positive outcome, 0 for negative).
        protected_attribute (str): The protected attribute to consider (e.g., 'gender', 'race').
    Returns:
        dict: Keys are each unique value in column protected_attribute. Values are disparate impact ratio.
    """
    di_by_attribute = {}
    for attribute in df[protected_attribute].unique():
        # Probability of favorable outcome for privileged group
        prob_privileged = df[(df[protected_attribute] != attribute) & (df[outcome_column] == 1)].shape[0] / df[df[protected_attribute] == privileged_value].shape[0]

        # Probability of favorable outcome for unprivileged group
        prob_unprivileged = df[(df[protected_attribute] == attribute) & (df[outcome_column] == 1)].shape[0] / df[df[protected_attribute] == unprivileged_value].shape[0]

        # Calculate disparate impact
        di_by_attribute[attribute] = prob_unprivileged / prob_privileged
    return di_by_attribute

def calculate_statistical_parity_difference(dataset, protected_attribute, privileged_value, unprivileged_value, prediction_var, favorable_outcome):
    """ 
    Calculate statistical parity difference for pandas table that includes protected attribute and prediction. 
    
    Args:
        df (pd.Dataframe): DataFrame containing the data.
        protected_attribute (str): Column name of targeted attribute in DataFrame.
        privileged_value (str or int): The value of the protected attribute that represents the privileged group.
        unprivileged_value (str or int): The value of the protected attribute that represents the unprivileged group.
        prediction_var (str): Column name of prediction attribute in DataFrame
        favorable_outcome (str or int): Value of a positive outcome in prediction column.
    Returna:
        float: Statistical parity difference.
    """
    # Probability of the minority group
    prob_minority = (dataset[dataset[protected_attribute] == unprivileged_value][prediction_var]
                    == favorable_outcome).mean()
    # Probability of the majority group
    prob_majority = (dataset[dataset[protected_attribute] != privileged_value][prediction_var]
                    == favorable_outcome).mean()
    # Calculate statistical parity difference
    return prob_minority - prob_majority

def calculate_statistical_parity_difference_dict(dataset, protected_attribute, prediction_var, favorable_outcome):
    """ 
    Calculate statistical parity difference for pandas table that includes protected attribute and prediction. 
    
    Args:
        df (pd.Dataframe): DataFrame containing the data.
        protected_attribute (str): Column name of targeted attribute in DataFrame.
        prediction_var (str): Column name of prediction attribute in DataFrame
        favorable_outcome (str or int): Value of a positive outcome in prediction column.
    Returna:
        dict: Keys are each unique value in column protected_attribute. Values are statistical parity difference.
    """
    spd_by_attribute = {}
    for attribute in dataset[protected_attribute].unique():
        # Probability of the minority group
        prob_minority = (dataset[dataset[protected_attribute] == attribute][prediction_var]
                        == favorable_outcome).mean()
        # Probability of the majority group
        prob_majority = (dataset[dataset[protected_attribute] != attribute][prediction_var]
                        == favorable_outcome).mean()
        # Calculate statistical parity difference
        spd_by_attribute[attribute] = prob_minority - prob_majority
    return spd_by_attribute
