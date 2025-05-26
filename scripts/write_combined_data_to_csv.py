
# Script to merge the data from both sheets in Online_Retail_II and write it to a CSV file for greater performance.

import pandas as pd

# Load the first sheet (2009–2010)
print("Stage 1a - Reading in first Online Retail II sheet")
sheet1_df = pd.read_excel("../data/online_retail_II/online_retail_II.xlsx", sheet_name="Year 2009-2010")
# Load the second sheet (2010-2011)
print("Stage 1b - Reading in second Online Retail II sheet")
sheet2_df = pd.read_excel("../data/online_retail_II/online_retail_II.xlsx", sheet_name="Year 2010-2011")

# Combine both sheets into a single DataFrame (they have the same format)

print("Stage 2 - Combining both sheets into a single dataset")
combined_df = pd.concat([sheet1_df, sheet2_df], ignore_index=True)

# Write the combined DataFrame to a CSV file
print("Stage 3 - Writing combined dataset to a CSV file")
combined_df.to_csv("../outputs/csv/online_retail_II_combined.csv", index=False)
