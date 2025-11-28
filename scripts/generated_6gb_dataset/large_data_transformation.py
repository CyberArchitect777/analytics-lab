# An example of a data transformation techniques on a very large dataset
# requiring efficient memory usage.

from datetime import datetime, timedelta	
import os
import pandas as pd
import random
import string
import dask.dataframe as dd
import polars as pl
import psutil
from pathlib import Path
from dask import compute

def generate_dataset():
	if not os.path.exists("../../outputs/csv/generated_big_file.csv"):
		print("\nGenerating large dataset...\n")
		total_rows = 150000000
		chunk_size = 1000000
		current_chunk = 0
		while current_chunk <= total_rows:
			print("* Creating record " + str(current_chunk+1) + " to " + str(current_chunk + 1000000))
			big_data = {
		    	"AccountCode": [random.randint(10000, 99999) for _ in range(chunk_size)],
		    	"TransactionID": [i + 1 + chunk_size for i in range(chunk_size)],
		    	"Net": [round(random.uniform(0, 100), 2) for _ in range(chunk_size)],
		    	# _ is a placeholder, not an accessible variable
		    	"Date": [
		    (datetime(2025, 1, 1) + timedelta(days=random.randint(0, 364))).strftime("%Y-%m-%d")
		    for _ in range(chunk_size)],
		    	"Reference": ["".join(random.choices(string.ascii_uppercase + string.digits, k=8)) for _ in range(chunk_size)],
			}
			chunk_dataframe = pd.DataFrame(big_data)
			print("\n" + str(len(chunk_dataframe)) + " records in generated dataset")
			if current_chunk == 0:
				chunk_dataframe.to_csv("../../outputs/csv/generated_big_file.csv", index=False, encoding="utf-8", lineterminator="\n", header=True)
			else:
				chunk_dataframe.to_csv("../../outputs/csv/generated_big_file.csv", mode="a", index=False, encoding="utf-8", lineterminator="\n", header=False)
			current_chunk += 1000000
	else:
		# Count number of lines in existing file
		with open("../../outputs/csv/generated_big_file.csv", "r", encoding="utf-8") as f:
			line_count = sum(1 for line in f) - 1  # subtract 1 for header
		print(f"\nUsing previously generated large dataset with {line_count} records.\n")
	

def dask_transformation():
	print("\nStarting memory usage: " + provide_memory_usage_in_megabytes())
	df = dd.read_csv("../../outputs/csv/generated_big_file.csv", dtype={"AccountCode": "int64", "TransactionID": "int64", "Net": "float64", "Date": "object", "Reference": "object"})
	total_transactions, january_transactions, net_sum = compute(df.shape[0], 
															 	df[df["Date"].str.startswith("2025-01")].shape[0], 
															 	df.groupby("AccountCode")["Net"].sum())
	print("Total transactions in dataset: " + str(total_transactions))
	print("Total transactions in January" + str(january_transactions))
	print("Total sum of Net column:" + str(net_sum))
	print("\nMemory usage after variable calculation: " + provide_memory_usage_in_megabytes())
	df["Promotion"] = df["Net"] * (random.random() * 0.2)
	df["Same Day Transactions"] = df.groupby("Date")["TransactionID"].transform("count")
	df.compute()
	print("Memory usage after transformation: " + provide_memory_usage_in_megabytes())
	output_dataset_to_html(df.compute(), "../../outputs/html/dask_preview1.html")

def polars_transformation():
	pass

def chunked_pandas_transformation():
	pass

def output_dataset_to_html(df: pd.DataFrame, filename: str) -> None:
	# Simple HTML export of the provided dataset. na_rep is the string to use for NaN/NaT values
	html_str = df.head(1000).to_html(index=False, border=0, justify="left", na_rep="")
	Path(filename).write_text(html_str, encoding="utf-8")

def provide_memory_usage_in_megabytes() -> str:
	process = psutil.Process(os.getpid())
	# rss = Resident Set Size
	memory_info = round((process.memory_info().rss) / (1024 ** 2), 2)
	return str(memory_info) + "MB"

if __name__ == "__main__":
	print("\nStage 1 - Generate 6GB dataset for large file testing and write to CSV (if file doesn't exist)")
	generate_dataset()
	print("Stage 2 - Conduct data transformation using Dask")
	dask_transformation()
	print("Stage 3 - Conduct data transformation using Polars")
	polars_transformation()
	print("Stage 4 - Conduct data transformation using Chunked Pandas Reading")
	chunked_pandas_transformation()
	