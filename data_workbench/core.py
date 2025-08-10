
# Library script to provide a number of data transformation functions for generic use

import pandas as pd

def load_csv(file_path: str) -> tuple[int, pd.DataFrame]:

    """
    Load a CSV file into a DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    tuple[int, pd.DataFrame]: A tuple containing a status code (0 for success, 1 for failure) and the loaded DataFrame.
    """

    try:
        df = pd.read_csv(file_path)
        return 0, df
    except FileNotFoundError:
        return 1, pd.DataFrame()  # Return an empty DataFrame if the file is not found
    
def load_excel(file_path: str, sheet_name: str = None) -> tuple[int, pd.DataFrame]:
    
    """
    Load an Excel file into a DataFrame.

    Parameters:
    file_path (str): The path to the Excel file.
    sheet_name (str, optional): The name of the sheet to load. If None, loads the first sheet.
    
    Returns:
    tuple[int, pd.DataFrame]: A tuple containing a status code (0 for success, 1 for failure) and the loaded DataFrame.
    """

    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return 0, df
    except FileNotFoundError:
        return 1, pd.DataFrame()  # Return an empty DataFrame if the file is not found
    
def save_to_excel(df: pd.DataFrame, file_path: str, sheet_name: str = 'Sheet1') -> int:
    """
    Save a DataFrame to an Excel file.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path where the Excel file will be saved.
    sheet_name (str, optional): The name of the sheet in the Excel file. Defaults to 'Sheet1'.

    Returns:
    int: 0 if the file was saved successfully, 1 if there was an error
    """

    try:
        df.to_excel(file_path, sheet_name=sheet_name, index=False)
        return 0
    except Exception as e:
        return 1
    
def save_to_csv(df: pd.DataFrame, file_path: str) -> int:
    """
    Save a DataFrame to a CSV file.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path where the CSV file will be saved.

    Returns:
    int: 0 if the file was saved successfully, 1 if there was an error
    """

    try:
        df.to_csv(file_path, index=False)
        return 0
    except Exception as e:
        return 1

def display_dataframe_info(df: pd.DataFrame) -> tuple[int, str]:
    """
    Display basic information about the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.

    Returns:
    tuple[int, str]: A tuple containing a status code (0 for success, 1 for failure) and a string with the textual output for the user.
    """

    output_text = "\nDataFrame Information:" + df.info()
    output_text += output_text + "\nFirst 5 Rows:" + df.head()
    output_text += output_text + "\nStatistical Summary: " + df.describe()
    output_text += output_text + "\nNull Values Count: " + df.isnull().sum()
    output_text += output_text + "\nData Types: " + df.dtypes
    
    for column in df.columns:
        output_text += output_text + "\nValue Counts for '{column}':"
        output_text += output_text + df[column].value_counts().head(5)  # Display top 5 most common values
        output_text += output_text + df[column].value_counts().tail(5)  # Display bottom 5 most rare values
        output_text += output_text + "\nUnique values count: " + str(df[column].nunique())

    return 0, output_text

def show_first_x_records(df: pd.DataFrame, x: int) -> tuple[int, str]:
    """
    Display the first x records of the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to display.
    x (int): The number of records to display.

    Returns:
    tuple[int, pd.DataFrame]: A tuple containing a status code (0 for success, 1 for failure) and the DataFrame with the first x records.
    """

    if x <= 0:
        return 1, ""
    else:
        return 0, df.head(x)
    
def remove_columns_via_list(df: pd.DataFrame, column_names: list) -> tuple[int, pd.DataFrame]:
    """
    Remove specified columns from the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame from which to remove the columns.
    column_names (list): A list of column names to remove.

    Returns:
    tuple[int, list]: A tuple containing a status code (0 for success, 1 for failure) and a list containing all columns actually removed.
    """

    existing_columns = [col for col in column_names if col in df.columns]
    
    if existing_columns:
        df = df.drop(columns=existing_columns)
        return 0, existing_columns
    else:
        return 1, []

# Continue converting interface style from textual output to returned values from here.

def remove_records_via_index_range(df: pd.DataFrame, start_index: int, records_to_remove: int) -> int:
    """
    Remove records from the DataFrame by index range.

    Parameters:
    df (pd.DataFrame): The DataFrame from which to remove the records.
    start_index (int): The starting index of the range to remove.
    records_to_remove (int): The number of records to remove starting from the start_index.

    Returns:
    int: 0 if the records were removed successfully, 1 if there was an error
    """

    end_index = start_index + records_to_remove
    if start_index < 0 or end_index >= len(df):
        return 1
    
    indices_to_remove = list(range(start_index, end_index + 1))
    
    df = df.drop(index=indices_to_remove)
    return 0

def sort_fields(df: pd.DataFrame, sort_by: str, ascending: bool = True) -> tuple[int, pd.DataFrame]:
    """
    Sort the DataFrame by a specified field.

    Parameters:
    df (pd.DataFrame): The DataFrame to sort.
    sort_by (str): The column name to sort by.
    ascending (bool): Whether to sort in ascending order. Defaults to True.

    Returns:
    tuple[int, pd.DataFrame]: A tuple containing a status code (0 for success, 1 for failure) and the sorted DataFrame.
    """

    if sort_by not in df.columns:
        return 1, pd.DataFrame()
    
    df = df.sort_values(by=sort_by, ascending=ascending)
    return 0, df
