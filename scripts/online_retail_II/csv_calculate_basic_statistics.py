
# Script to read a compiled CSV version of the Online Retail II dataset and calculate basic statistics

import pandas as pd

# Load combined CSV file (this will need to have created by write_combined_data_to_csv.py first)

print("\nStage 1 - Read in the Online Retail II CSV file")
combined_df = pd.read_csv("../../outputs/csv/online_retail_II_combined.csv")

# Calculate the total sales

print("\nStage 2 - Calculate total sales")
total_sales = combined_df["Quantity"] * combined_df["Price"]
print("\nTotal Sales: {:.2f}".format(total_sales.sum()))

# Print the top five products by total sales amount

print("\nStage 3 - Top five products by total sales amount")

# First, create a Revenue column by multiplying Quantity and Price
combined_df["Revenue"] = combined_df["Quantity"] * combined_df["Price"]

top_products = (combined_df
    .groupby("StockCode")
    .agg({"Revenue": "sum"})
    .sort_values('Revenue', ascending=False)
    .head(5)
)

print(top_products)

# Find the top five days that had the most sales

print("\nStage 4 - Top five days with the most sales")

top_days = (combined_df
    .groupby("InvoiceDate")
    .agg({"Revenue": "sum"})
    .sort_values('Revenue', ascending=False)
    .head(5)
)

print(top_days)
