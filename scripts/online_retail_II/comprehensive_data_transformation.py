# An example of a data transformation using a variety of tools

import pandas as pd
from pathlib import Path

def start_transform() -> None:
	# Input Excel
	#print("\nStage 1 - Read Excel file...")
	#df1 = pd.read_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name=0)
	#df2 = pd.read_excel("../../data/online_retail_II/online_retail_II.xlsx", sheet_name=1)
	# Input CSV
	
	print("\nStage 1 - Read CSV file...")
	df_joined = pd.read_csv("../../outputs/csv/online_retail_II_combined.csv", encoding="utf-8")
	# Print Excel sheet sizes in rows and columns
	#print("Stage 2a - Excel 1 Rows/columns - " + str(df1.shape))
	#print("Stage 2b - Excel 2 Rows/columns - " + str(df2.shape))
	# Combine the two Excel sheets into one dataset
	#df_joined = pd.concat([df1, df2])
	# Print combined dataset size in rows and columns
	
	print("Stage 2 - Rows/columns - " + str(df_joined.shape))
	# Output file to CSV
	#print("Stage 2c - Write CSV...")
	#df_joined.to_csv("../../outputs/csv/online_retail_II_combined.csv", index=False, encoding="utf-8", lineterminator="\n")
	# Write out a dataset table listing to html
	
	print("Stage 3 - Output column statistical data for numerical fields\n")
	print(df_joined.describe().to_string())
	
	print("\nStage 4 - Show data columns and types\n")
	print(df_joined.dtypes)
	
	print("\nStage 5 - Change data type of Customer ID to string")
	df_joined = df_joined.astype({"Customer ID": "str"})
	
	print("Stage 6 - Clean up Customer ID field")
	# Extract only numbers at the start of the field and replace blanks with -1
	df_joined["Customer ID"] = df_joined["Customer ID"].str.extract(r"(\d+)")
	df_joined["Customer ID"] = df_joined["Customer ID"].fillna("-1")
	
	print("Stage 7 - Clean up date field into dd-mm-yyy format")
	df_joined["InvoiceDate"] = pd.to_datetime(df_joined["InvoiceDate"])
	df_joined["InvoiceDate"] = df_joined['InvoiceDate'].dt.strftime("%d-%m-%Y")
	
	print("Stage 8 - Select only a few fields")
	df_subset = df_joined[["StockCode", "Description", "Price"]].copy()
	
	print("Stage 9 - Output subset dataset table to HTML")
	output_dataset_to_html(df_subset, "../../outputs/html/preview1.html")
	
	print("Stage 10 - Sort by StockCode")
	df_subset = df_subset.sort_values(by=["StockCode","Price"], ascending=[True,True])
	
	print("Stage 11 - Output preview2.html")
	output_dataset_to_html(df_subset, "../../outputs/html/preview2.html")
	
	print("Stage 12 - Find duplicates\n")
	print("Pre-Duplicate Remove Dataset: " + str(df_subset.shape))
	df_subset = df_subset.drop_duplicates(subset=["StockCode"], keep="first")
	print("Post-Duplicate Remove Dataset: " + str(df_subset.shape))
	
	print("\nStage 13 - Output preview3.html")
	output_dataset_to_html(df_subset, "../../outputs/html/preview3.html")
	
	print("Stage 14 - Group by Invoice to get total Price per Invoice")
	# Without reset_index, the groupby becomes the index, otherwise the index is numerical.
	df_group = df_joined.groupby("Invoice").agg(Total_Price=("Price","sum")).reset_index() 
	
	print("Stage 15 - Rename Total_Price to Total Price")
	df_group = df_group.rename(columns={"Total_Price":"Total Price"})
	
	print("Stage 16 - Output preview4.html")
	output_dataset_to_html(df_group, "../../outputs/html/preview4.html")
	
	print("Stage 17 - Filter Invoice field by single value")
	df_filtered = df_joined.query("Invoice == '489434'")
	
	print("Stage 18 - Output preview5.html")
	output_dataset_to_html(df_filtered, "../../outputs/html/preview5.html")
	# Main preview output
	
	print("\nLast stage - Output main dataset table to HTML\n")
	output_dataset_to_html(df_joined, "../../outputs/html/preview.html")
	
def output_dataset_to_html(df: pd.DataFrame, filename: str) -> None:
	# Simple HTML export of the provided dataset
	html_str = df.head(1000).to_html(index=False, border=0)
	Path(filename).write_text(html_str, encoding="utf-8")
	
if __name__ == "__main__":
	start_transform()