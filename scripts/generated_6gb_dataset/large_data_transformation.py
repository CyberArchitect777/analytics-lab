# An example of a data transformation techniques on a very large dataset
# requiring efficient memory usage.

from datetime import datetime, timedelta	
import os
import pandas as pd
import random
import string
import dask.dataframe as dd
import polars as pl

def generate_dataset():
	if not os.path.exists("../../outputs/csv/generated_big_file.csv"):
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
			if current_chunk == 0:
				chunk_dataframe.to_csv("../../outputs/csv/generated_big_file.csv", index=False, encoding="utf-8", lineterminator="\n", header=True)
			else:
				chunk_dataframe.to_csv("../../outputs/csv/generated_big_file.csv", mode="a", index=False, encoding="utf-8", lineterminator="\n", header=False)
			current_chunk += 1000000

def dask_transformation():
	pass

def polars_transformation():
	pass

def chunked_pandas_transformation():
	pass

if __name__ == "__main__":
	print("Stage 1 - Generate 6GB dataset for large file testing and write to CSV (if file doesn't exist)")
	generate_dataset()
	print("Stage 2 - Conduct data transformation using Dask")
	dask_transformation()
	print("Stage 3 - Conduct data transformation using Polars")
	polars_transformation()
	print("Stage 4 - Conduct data transformation using Chunked Pandas Reading")
	chunked_pandas_transformation()
	