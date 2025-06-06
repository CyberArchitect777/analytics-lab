
# Program to provide a number of data transformation functions for generic use

import pandas as pd

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """

    try:
        df = pd.read_csv(file_path)
        print(f"CSV file '{file_path}' loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found
    
def load_excel(file_path: str, sheet_name: str = None) -> pd.DataFrame:
    """
    Load an Excel file into a DataFrame.

    Parameters:
    file_path (str): The path to the Excel file.
    sheet_name (str, optional): The name of the sheet to load. If None, loads the first sheet.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """

    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Excel file '{file_path}' loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found
    
def save_to_excel(df: pd.DataFrame, file_path: str, sheet_name: str = 'Sheet1') -> None:
    """
    Save a DataFrame to an Excel file.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path where the Excel file will be saved.
    sheet_name (str, optional): The name of the sheet in the Excel file. Defaults to 'Sheet1'.
    """

    try:
        df.to_excel(file_path, sheet_name=sheet_name, index=False)
        print(f"DataFrame saved to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while saving to Excel: {e}")
    
def save_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """
    Save a DataFrame to a CSV file.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path where the CSV file will be saved.
    """

    try:
        df.to_csv(file_path, index=False)
        print(f"DataFrame saved to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

def display_dataframe_info(df: pd.DataFrame) -> None:
    """
    Display basic information about the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.
    """

    print("\nDataFrame Information:")
    df.info()
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nStatistical Summary:")
    print(df.describe())
    print("\nNull Values Count:")
    print(df.isnull().sum())
    print("\nData Types:")
    print(df.dtypes)
    
    for column in df.columns:
        print(f"\nValue Counts for '{column}':")
        print(df[column].value_counts().head(5))  # Display top 5 most common values
        print(df[column].value_counts().tail(5))  # Display bottom 5 most rare values
        print(f"Unique values count: {df[column].nunique()}")

def remove_columns_via_list(df: pd.DataFrame, column_names: list) -> pd.DataFrame:
    """
    Remove specified columns from the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame from which to remove the columns.
    column_names (list): A list of column names to remove.

    Returns:
    pd.DataFrame: The DataFrame with the specified columns removed.
    """

    existing_columns = [col for col in column_names if col in df.columns]
    
    if existing_columns:
        df = df.drop(columns=existing_columns)
        print(f"Columns {existing_columns} removed successfully.")
    else:
        print("None of the specified columns exist in the DataFrame.")
    
    return df

def remove_records_via_index_range(df: pd.DataFrame, start_index: int, end_index: int) -> pd.DataFrame:
    """
    Remove records from the DataFrame by index range.

    Parameters:
    df (pd.DataFrame): The DataFrame from which to remove the records.
    start_index (int): The starting index of the range to remove.
    end_index (int): The ending index of the range to remove.

    Returns:
    pd.DataFrame: The DataFrame with the specified records removed.
    """

    if start_index < 0 or end_index >= len(df):
        print("Invalid index range specified.")
        return df
    
    indices_to_remove = list(range(start_index, end_index + 1))
    
    df = df.drop(index=indices_to_remove)
    print(f"Records from index {start_index} to {end_index} removed successfully.")
    
    return df

