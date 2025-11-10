def print_unique_categorical(df):
    """
    Prints unique values for each categorical column in a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to inspect
    """
    import pandas as pd
    
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    if len(categorical_cols) == 0:
        print("No categorical columns found.")
        return
    
    for col in categorical_cols:
        unique_vals = df[col].unique()
        print(f"\nColumn '{col}' has {len(unique_vals)} unique values:")
        print(unique_vals)

def category_counts(df, exclude_cols=None):
    """
    Prints the number of rows for each category in all categorical columns,
    excluding specified columns (like IDs).
    
    Parameters:
    - df: pandas DataFrame
    - exclude_cols: list of columns to exclude (default: None)
    
    Returns:
    - A dictionary mapping column names to pandas Series of counts
    """
    if exclude_cols is None:
        exclude_cols = []
    
    # Select categorical columns excluding specified columns
    categorical_cols = [col for col in df.select_dtypes(include=['object', 'category']).columns
                        if col not in exclude_cols]
    
    counts_dict = {}
    for col in categorical_cols:
        counts = df[col].value_counts()
        counts_dict[col] = counts
        print(f"\nColumn '{col}' counts:")
        print(counts)
    
    return counts_dict

def unique_categorical(df):
    """
    Prints unique values for each categorical column in a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to inspect
    """
    import pandas as pd
    
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    if len(categorical_cols) == 0:
        print("No categorical columns found.")
        return
    
    for col in categorical_cols:
        unique_vals = df[col].unique()
        print(f"\nColumn '{col}' has {len(unique_vals)} unique values:")

# Interpretation of Cohen's h
def interpret_cohens_h(h):
    h_abs = abs(h)
    if h_abs < 0.2:
        return "negligible"
    elif h_abs < 0.5:
        return "small"
    elif h_abs < 0.8:
        return "medium"
    else:
        return "large"