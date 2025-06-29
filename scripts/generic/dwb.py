
# Data Workbench command-line program for generic data processing tasks.

import sys
import os
import data_workbench_library as dw

def help():
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
    print("--help = Help\n")

def main():
    
    """
    The first function run upon program start to provide the command-line interface
    """
    
    print("\nData Workbench")
    print("Version 0.1.0")
    print("By Barrie Millar")
    print("A script to perform generic data transformation tasks\n")

    if len(sys.argv) > 1 and check_file_path(sys.argv[1]):
        absolute_path = os.path.abspath(sys.argv[1])

    if len(sys.argv) == 1:
        help()
        sys.exit(1)
    elif len(sys.argv) == 2:
        display_info(absolute_path)
    elif len(sys.argv) == 3:
        command = sys.argv[2]
        if command == "--display-info":
            display_info(absolute_path)
        elif command == "--first-x-records":
            print("Please provide the number of records to display")
    else:
        command = sys.argv[2]
        if command == "--display-info":
            display_info(absolute_path)
        elif command == "--first-x-records":
            try:
                x = int(sys.argv[3])
                display_first_x_records(absolute_path, x)
            except ValueError:
                print("Please provide a valid integer for the number of records to display.")
                sys.exit(1)
        elif command == "--remove-columns-by-name":
            column_names = sys.argv[3:]
            remove_columns_by_name(absolute_path, column_names)

def check_file_path(file_path):
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

def load_file(file_path):
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
    
def save_file(df, file_path):
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

def detect_extension(file_path):
    """
    Detect the file extension of the given file path.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    str: The file extension (e.g., 'csv', 'xlsx').
    """
    
    _, ext = os.path.splitext(file_path)
    return ext.lower().replace('.', '')

def is_valid_extension(file_path):
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

def display_info(file_path):
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

def display_first_x_records(file_path, x):
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


def remove_columns_by_name(file_path, column_names):
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

if __name__ == "__main__":
    
    """
    Runs the main function if this code is being run directly.
    """
    
    main()
