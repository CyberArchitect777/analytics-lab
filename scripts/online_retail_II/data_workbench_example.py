
# Script to test and demostrate Data Workbench on the Online Retail II dataset

import pandas as pd
import sys

sys.path.append("../generic")
import data_workbench as dw

print("\nStage 1 - Loading both Online Retail II Excel sheets (disabled for performance)")

#online_retail_II_2009 = dw.load_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name="Year 2009-2010")
#online_retail_II_2010 = dw.load_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name="Year 2010-2011")

print("\nStage 2 - Loading merged CSV Online Retail II file\n")

online_retail_II_combined = dw.load_csv("../../outputs/csv/online_retail_II_combined.csv")

print("\nStage 3 - Displaying DataFrame information for the combined CSV")

dw.display_dataframe_info(online_retail_II_combined)

print("\nStage 4 - Display the first five rows alone")

dw.show_first_x_records(online_retail_II_combined, 5)

print("\nStage 5 - Remove the description field")

online_retail_II_combined = dw.remove_columns_via_list(online_retail_II_combined, ["Description"])

print("\nStage 6 - Display the first five rows again")

dw.show_first_x_records(online_retail_II_combined, 5)

print("\nStage 7 - Remove all but first 3 rows")

online_retail_II_combined = dw.remove_records_via_index_range(online_retail_II_combined, 3, 1067370)

print("\nStage 8 - Display the first five rows again")

dw.show_first_x_records(online_retail_II_combined, 5)

print("\nStage 9 - Save the new CSV file to the outputs directory")

dw.save_to_csv(online_retail_II_combined, "../../outputs/csv/online_retail_II_data_workbench_example.csv")

print("\nStage 10 - Save the CSV data to an Excel spreadsheet")

dw.save_to_excel(online_retail_II_combined, "../../outputs/sheets/online_retail_II_data_workbench_example.xlsx", "Combined")