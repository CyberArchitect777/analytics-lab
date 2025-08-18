# An example of a data transformation using a variety of tools

import pandas as pd
from pathlib import Path

def start_transform() -> None:
	# Input Excel
	print("Stage 1 - Read Excel file...")
	df1 = pd.read_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name=0)
	df2 = pd.read_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name=1)
	# Input CSV
	#print("Stage 1 - Read CSV file...")
	#df_joined = pd.read_csv("../../outputs/csv/online_retail_II_combined.csv", encoding="utf-8")
	# Print Excel sheet sizes in rows and columns
	print("Stage 2a - Excel 1 Rows, columns" + str(df1.shape))
	print("Stage 2b - Excel 2 Rows, columns" + str(df2.shape))
	# Combine the two Excel sheets into one dataset
	df_joined = pd.concat([df1, df2])
	# Print combined dataset size in rows and columns
	#print("Stage 2 - Rows/columns - " + str(df_joined.shape))
	# Output file to CSV
	print("Stage 2c - Write CSV...")
	df_joined.to_csv("online_retail_II.csv", index=False, encoding="utf-8", lineterminator="\n")
	# Write out a dataset table listing to html
	print("Stage 3 - Output dataset table to HTML")
	output_dataset_to_html(df_joined, "../../outputs/html/preview.html")
	print("Stage 4 - Output column statistical data for numerical fields\n")
	print(df_joined.describe().to_string())
	print("\nStage 5 - Show data columns and types\n")
	print(df_joined.dtypes)
	
def output_dataset_to_html(df: pd.DataFrame, filename: str) -> None:
	# Simple HTML export of the provided dataset
	html_str = df.head(1000).to_html(index=False, border=0)
	Path(filename).write_text(html_str, encoding="utf-8")
	
if __name__ == "__main__":
	start_transform()