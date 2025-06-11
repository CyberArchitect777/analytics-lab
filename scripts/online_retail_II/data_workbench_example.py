
# Script to test and demostrate Data Workbench on the Online Retail II dataset

import pandas as pd
import sys
import data_workbench_library as dwl

sys.path.append("../generic")

print("\nStage 1 - Loading both Online Retail II Excel sheets (disabled for performance)")

#online_retail_II_2009 = dwl.load_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name="Year 2009-2010")
#online_retail_II_2010 = dwl.load_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name="Year 2010-2011")

print("\nStage 2 - Loading merged CSV Online Retail II file\n")

online_retail_II_combined = dwl.load_csv("../../outputs/csv/online_retail_II_combined.csv")

print("\nStage 3 - Displaying DataFrame information for the combined CSV")

dwl.display_dataframe_info(online_retail_II_combined)

print("\nStage 4 - Display the first five rows alone")

dwl.show_first_x_records(online_retail_II_combined, 5)

print("\nStage 5 - Remove the description field")

online_retail_II_combined = dwl.remove_columns_via_list(online_retail_II_combined, ["Description"])

print("\nStage 6 - Display the first five rows again")

dwl.show_first_x_records(online_retail_II_combined, 5)

print("\nStage 7 - Remove all but first 3 rows")

online_retail_II_combined = dwl.remove_records_via_index_range(online_retail_II_combined, 3, 1067370)

print("\nStage 8 - Display the first five rows again")

dwl.show_first_x_records(online_retail_II_combined, 5)

print("\nStage 9 - Save the new CSV file to the outputs directory")

dwl.save_to_csv(online_retail_II_combined, "../../outputs/csv/online_retail_II_data_workbench_example.csv")

print("\nStage 10 - Save the CSV data to an Excel spreadsheet")

dwl.save_to_excel(online_retail_II_combined, "../../outputs/sheets/online_retail_II_data_workbench_example.xlsx", "Combined")