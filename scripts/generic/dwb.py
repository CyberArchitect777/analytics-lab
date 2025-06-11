
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
    print("\ndwb <command> <data file>")
    print("\nCommands:")
    print("--display-csv-info = Display information on a CSV file")
    print("--help = Help\n")

def main():
    
    """
    The first function run upon program start to provide the command-line interface
    """
    
    print("\nData Workbench")
    print("Version 0.1.0")
    print("By Barrie Millar")
    print("A script to perform generic data transformation tasks\n")

    if len(sys.argv) == 1:
        help()
        sys.exit(1)
    elif len(sys.argv) == 2:
        command = sys.argv[1]
        if command == "--display-csv-info":
            print("Please provide a CSV file path to display data information\n")
        else:
            help()
            sys.exit(1)
    else:
        command = sys.argv[1]
        filepath = sys.argv[2]
        if not os.path.exists(filepath):
            print("Please provide a valid filepath\n")
        else:
            absolute_path = os.path.abspath(filepath)
            if command == "--display-csv-info":
                display_csv_info(absolute_path)
            else:
                help()
                sys.exit(1)

def display_csv_info(file_path):
    """
    Display information about a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    """
    
    try:
        df = dw.load_csv(file_path)
        dw.display_dataframe_info(df)
    except Exception as e:
        print(f"An error occurred while processing the CSV file: {e}")

if __name__ == "__main__":
    
    """
    Runs the main function if this code is being run directly.
    """
    
    main()
