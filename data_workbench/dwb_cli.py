
# Data Workbench command-line version for generic data processing tasks.

import sys
import os
import core as dw
import pandas as pd

def help() -> None:
    """
    Outputs help information to the user if asked
    for or if an invalid function is specified
    """
    
    print("General usage:")
    print("\ndwb <data file> <command> <switches>")
    print("\nCommands:")
    print("--display-info = Display information on a input file")
    print("--first-x-records = Display the first x records of the input file")
    print("--remove-columns-by-name = Remove columns from the input file by name")
    print("--remove-records-by-index = Remove records by start index and number of records")

def main() -> None:
    
    """
    The first function run upon program start to provide the command-line interface
    """
    
    print("\nData Workbench")
    print("\nCommand-line edition")
    print("Version 0.1.0")
    print("By Barrie Millar")
    print("A script to perform generic data transformation tasks\n")

    # Assuming the first parameter is an input file, create a variable to set it to absolute
    # regardless of the original form.

    if len(sys.argv) > 1 and check_file_path(sys.argv[1]):
        absolute_path = os.path.abspath(sys.argv[1])

    if len(sys.argv) == 1: # If no arguments are provided, display help
        help()
        sys.exit(1)
    elif len(sys.argv) == 2: # If only a file is specified, display info on it.
        display_info(absolute_path)
    elif len(sys.argv) == 3: # Assume a path and command are provided with no parameters
        command = sys.argv[2]
        if command == "--display-info":
            display_info(absolute_path)
        elif command == "--first-x-records":
            print("Please provide the number of records to display\n")
        elif command == "--remove-columns-by-name":
            print("Please provide the names of the columns to remove\n")
        elif command == "--remove-records-by-index":
            print("Please provide the start index and number of records to remove\n")
    else: # Assume a file, command and at least one parameter are provided
        command = sys.argv[2]
        if command == "--display-info":
            display_info(absolute_path)
        elif command == "--first-x-records":
            try:
                x = int(sys.argv[3])
                display_first_x_records(absolute_path, x)
            except ValueError:
                print("Please provide a valid integer for the number of records to display.\n")
                sys.exit(1)
        elif command == "--remove-columns-by-name":
            column_names = sys.argv[3:]
            remove_columns_by_name(absolute_path, column_names)
        elif command == "--remove-records-by-index":
            try:
                start_index = int(sys.argv[3])
                records_to_remove = int(sys.argv[4])
                remove_records_by_index(absolute_path, start_index, records_to_remove)
            except ValueError:
                print("Please provide valid integers for the start index and number of records to be removed.\n")
                sys.exit(1)

def check_file_path(file_path: str) -> bool:
    """
    Check if the provided file path exists and has a valid extension.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    bool: True if the file exists and has a valid extension, False otherwise.
    """
    
    if not os.path.exists(file_path):
        print(f"File does not exist: {file_path}")
        sys.exit(1)
    
    if not is_valid_extension(file_path):
        print(f"Invalid file extension for: {file_path}")
        sys.exit(1)
    
    return True

def load_file(file_path: str) -> pd.DataFrame:
    """
    Load a file based on its extension.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    
    ext = detect_extension(file_path)
    
    if ext == 'csv':
        return dw.load_csv(file_path)
    elif ext == 'xlsx':
        return dw.load_excel(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
    
def save_file(df: pd.DataFrame, file_path: str) -> None:
    """
    Save a DataFrame to a file based on its extension.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path where the file will be saved.
    """
    
    ext = detect_extension(file_path)
    
    if ext == 'csv':
        dw.save_to_csv(df, file_path)
    elif ext == 'xlsx':
        dw.save_to_excel(df, file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def detect_extension(file_path: str) -> str:
    """
    Detect the file extension of the given file path.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    str: The file extension (e.g., 'csv', 'xlsx').
    """

    _, ext = os.path.splitext(file_path)
    return ext.lower().replace('.', '')

def is_valid_extension(file_path: str) -> bool:
    """
    Check if the file has a valid extension.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    bool: True if the file has a valid extension, False otherwise.
    """
    
    ext = detect_extension(file_path)
    if ext == 'csv' or ext == "xlsx":
        return True
    else:
        return False

def display_info(file_path: str) -> None:
    """
    Display information about the input file.
    
    Parameters:
    file_path (str): The path to the input file.
    """
    
    try:
        df = load_file(file_path)
        dw.display_dataframe_info(df)
    except Exception as e:
        print(f"An error occurred while processing the input file: {e}")

def display_first_x_records(file_path: str, x: int) -> None:
    """
    Display the first x records of the input file.
    
    Parameters:
    file_path (str): The path to the input file.
    x (int): The number of records to display.
    """
    
    try:
        df = load_file(file_path)
        dw.show_first_x_records(df, x)
    except Exception as e:
        print(f"An error occurred while processing the input file: {e}")

def remove_columns_by_name(file_path: str, column_names: list) -> None:
    """
    Remove specified columns from the input file by a list of names.
    
    Parameters:
    file_path (str): The path to the input file.
    column_names (list): A list of column names to remove.
    """
    
    try:
        df = load_file(file_path)
        df = dw.remove_columns_via_list(df, column_names)
        save_file(df, file_path)
    except Exception as e:
        print(f"An error occurred while processing the input file: {e}")

def remove_records_by_index(file_path: str, start_index: int, records_to_remove: int) -> None:
    """
    Remove records from the input file by index range.
    
    Parameters:
    file_path (str): The path to the input file.
    start_index (int): The starting index of the records to remove.
    records_to_remove (int): The number of records to remove starting from the start_index.
    """
    
    try:
        df = load_file(file_path)
        df = df.drop(df.index[start_index:records_to_remove + start_index])
        save_file(df, file_path)
    except Exception as e:
        print(f"An error occurred while processing the input file: {e}")

if __name__ == "__main__":
    
    """
    Runs the main function if this code is being run directly.
    """
    
    main()
