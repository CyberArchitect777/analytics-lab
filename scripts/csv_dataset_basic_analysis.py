
# Script to read a compiled CSV version of the Online Retail II dataset and conduct basic analysis on it.

import pandas as pd

# Load combined CSV file (this will need to have created by write_combined_data_to_csv.py first)

print("\nStage 1 - Read in the Online Retail II CSV file")
combined_df = pd.read_csv("../outputs/csv/online_retail_II_combined.csv")

# Start basic analysis of the data

print("\nStage 2 - Print out the DataFrame structure to gain insight into the number of records, columns and information about each one\n")
combined_df.info()
print("\nStage 3 - Display the first 5 rows of the combined dataset\n")
print(combined_df.head(5))
print("\nStage 4 - Print a statistical output of all numeric fields in the dataset\n")
print(combined_df.describe())
