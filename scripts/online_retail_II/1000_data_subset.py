
# Script to extract a smaller subset of records from the main dataset to make it more manageable on slower devices. 1000 records is the target

import pandas as pd

# Load the first sheet (2009–2010)
print("Stage 1a - Reading in first Online Retail II sheet")
sheet1_df = pd.read_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name="Year 2009-2010")

# Load the second sheet (2010–2011)
print("Stage 1b - Reading in second Online Retail II sheet")
sheet2_df = pd.read_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name="Year 2010-2011")

# Predictably sample 100 random records based on a seed

print("Stage 2 - Reducing dataset size for both sheets")
sheet1_reduced = sheet1_df.sample(n=1000, random_state=68)
sheet2_reduced = sheet2_df.sample(n=1000, random_state=68)

# Writing the reduced dataset to a new spreadsheet without a row index

print("Stage 3 - Output reduced datasets to new files")
sheet1_reduced.to_excel("../../outputs/sheets/online_retail_II_1000_records_0910.xlsx", index=False)
sheet2_reduced.to_excel("../../outputs/sheets/online_retail_II_1000_records_1011.xlsx", index=False)
