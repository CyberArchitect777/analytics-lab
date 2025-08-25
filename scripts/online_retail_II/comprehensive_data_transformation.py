# An example of a data transformation using a variety of tools

import pandas as pd
from glob import glob
from pathlib import Path
from chardet.universaldetector import UniversalDetector

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
	#df_joined["InvoiceDate"] = pd.to_datetime(df_joined["InvoiceDate"], format="%d-%m-%Y") # Specify date format

	# Datetime format codes:
	# %Y=4-digit year (2025), %y=2-digit year (25), %m=month 01-12, %B=full month (August), %b=abbr month (Aug), %d=day 01-31
	# %H=hour 00-23, %I=hour 01-12, %p=AM/PM, %M=minute 00-59, %S=second 00-59, %f=microseconds 000000-999999
	# %z=UTC offset (+0000), %Z=timezone (UTC), %j=day of year 001-366, %U=week num (Sunday first), %W=week num (Monday first)
	#
	# Common patterns:
	# "%Y-%m-%d"→2025-08-25, "%d-%m-%Y"→25-08-2025, "%m/%d/%Y"→08/25/2025
	# "%d/%m/%Y %H:%M:%S"→25/08/2025 14:30:00, "%Y-%m-%d %H:%M:%S"→2025-08-25 14:30:00
	# "%d-%b-%Y"→25-Aug-2025, "%b %d, %Y"→Aug 25, 2025
	
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
	# aggfunc includes things like "sum", "mean", "count", "min", "max", "median"
	df_group = df_joined.groupby("Invoice").agg(Total_Price=("Price","sum")).reset_index() 
	
	print("Stage 15 - Rename Total_Price to Total Price")
	df_group = df_group.rename(columns={"Total_Price":"Total Price"})
	
	print("Stage 16 - Output preview4.html")
	output_dataset_to_html(df_group, "../../outputs/html/preview4.html")
	
	print("Stage 17 - Filter Invoice field by single value")
	df_filtered = df_joined.query("Invoice == '489434'")
	
	print("Stage 18 - Output preview5.html")
	output_dataset_to_html(df_filtered, "../../outputs/html/preview5.html")

	print("Stage 19 - Provide a random sample output")
	df_random = df_joined.sample(n=100, random_state=42355)

	print("Stage 20 - Output preview6.html")
	output_dataset_to_html(df_random, "../../outputs/html/preview6.html")

	print("Stage 21 - Create new fields Total_Price and Over_100 and calculate them using formulas")
	df_joined = df_joined.assign(Total_Price=lambda x: x["Price"]*x["Quantity"], Over_100=lambda x: x["Total_Price"]>100)

	print("Stage 22 - Create two new datasets")
	dict_one = {
		 "user_id": ["ab", "az"],
		 "name": ["Bryan", "Claire"]
	}
	dict_two = {
		 "user_id": ["ab", "az"],
		 "position": ["senior", "junior"]
	}
	df1 = pd.DataFrame(dict_one)
	df2 = pd.DataFrame(dict_two)

	print("Stage 23 - Join the two new datasets by user_id")
	df_merged = df1.merge(df2, on=["user_id"], how="inner", suffixes=("","_r"))

	print("Stage 24 - Output preview7.html")
	output_dataset_to_html(df_merged, "../../outputs/html/preview7.html")

	print("Stage 25 - Append field from one dataset to another")
	dict_three = {
		"Employed": ["yes"]
	}
	df3 = pd.DataFrame(dict_three)
	df_merged = df_merged.merge(df3, how="cross")

	print("Stage 26 - Output preview8.html")
	output_dataset_to_html(df_merged, "../../outputs/html/preview8.html")

	print("Stage 27 - Find and replace text in a dataset field")
	df_findreplace = df_joined.copy()
	df_findreplace["Customer ID"] = df_findreplace["Customer ID"].str.replace("13085", "99999", regex=False)

	print("Stage 28 - Output preview9.html")
	output_dataset_to_html(df_findreplace, "../../outputs/html/preview9.html")

	print("Stage 29 - Create a new dataset and apply crosstab")
	sample_dataset = {
    "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT", "Sales", "IT", "HR"],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Male", "Female", "Female"],
    "Hired": ["Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes"]
	}
	df_sample_dataset = pd.DataFrame(sample_dataset)
	df_sample_dataset = pd.pivot_table(df_sample_dataset, index="Gender", columns="Department", values="Hired", aggfunc="count").reset_index()

	print("Stage 30 - Output preview10.html")
	output_dataset_to_html(df_sample_dataset, "../../outputs/html/preview10.html")

	print("Stage 31 - Select a few records and then transpose the main dataset to a new one")
	df_transposed = df_joined.iloc[0:10]
	df_transposed = df_transposed.transpose()

	print("Stage 32 - Output preview11.html")
	output_dataset_to_html(df_transposed, "../../outputs/html/preview11.html")

	print("Stage 33 - Breaking up a data field into columns")

	csv_test_file = {
		 "field": [ "All data,is,here" ],
	}
	csv_test_data = pd.DataFrame(csv_test_file)
	# n=1 specifies how many splits to perform, the rest are left in the last column. Expand = true sets the return as a DataFrame rather than a list of Series types
	# Adds to csv_test_data
	csv_test_data[["Field1", "Field2", "Field3"]] = csv_test_data["field"].str.split(",", n=3, expand=True)

	print("Stage 34 - Output preview12.html")
	output_dataset_to_html(csv_test_data, "../../outputs/html/preview12.html")

	print("Stage 35 - Explore regex operations using copy dataset")
	df_regex_work = df_joined.copy()
	df_regex_work["Country"] = df_regex_work["Country"].str.replace(r"United Kingdom", "UK", regex=True)
	df_regex_work["InvoiceDate"] = df_regex_work["InvoiceDate"].str.extract(r"(\d{4})")
	df_regex_work = df_regex_work.astype({"Price": "str"})
	df_regex_work["Is_Price_x.xx_Format"] = df_regex_work["Price"].str.match(r"^\d\.\d{2}.*$")

	print("Stage 36 - Output preview13.html")
	output_dataset_to_html(df_regex_work, "../../outputs/html/preview13.html")

	print("Stage 37 - Add unique key to main dataset")
	df_joined = df_joined.reset_index(drop=True); df_joined["RecordID"] = df_joined.index + 1

	print("Stage 38 - Read in multiple CSV files and process them")
	csv_files = glob("../../outputs/csv/*.csv")
	df_freshread = pd.read_csv("../../outputs/csv/online_retail_II_combined.csv", encoding="utf-8")
	df_list = [pd.read_csv(file) for file in csv_files]
	df_all = pd.concat(df_list, ignore_index=True)
	
	print("Stage 39 - Rows/columns - " + str(df_freshread.shape))
	print("Stage 40 - Rows/columns - " + str(df_all.shape))

	print("Stage 41 - Read in CSV file with automatic detection of encoding")

	detector = UniversalDetector()
	with open("../../outputs/csv/online_retail_II_combined.csv", "rb") as f:
		for line in f:
			detector.feed(line)
			if detector.done:
				break
	detector.close()
	enc = detector.result.get("encoding") or "utf-8"
	confidence = detector.result.get("confidence")
	print("\nGuessed encoding: ", enc, "with confidence: ", confidence)
	# errors can be replace, ignore or strict. 
	# Replace changes unreadable for placeholder, strict flags errors
	with open("../../outputs/csv/online_retail_II_combined.csv", encoding=enc, errors="replace") as f:
		df_test = pd.read_csv(f)

	print("Stage 42 - Display the first three rows:\n")
	print(df_joined.head(3).to_string())

	print("\nStage 43 - Display the last three rows:\n")
	print(df_joined.tail(3).to_string())

	# Main preview output
	print("\nLast stage - Output main dataset table to HTML\n")
	output_dataset_to_html(df_joined, "../../outputs/html/preview.html")
	
def output_dataset_to_html(df: pd.DataFrame, filename: str) -> None:
	# Simple HTML export of the provided dataset
	html_str = df.head(1000).to_html(index=False, border=0)
	Path(filename).write_text(html_str, encoding="utf-8")
	
if __name__ == "__main__":
	start_transform()