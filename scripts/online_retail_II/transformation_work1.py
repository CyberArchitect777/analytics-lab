# Transformation work 1
# An example of a targetted data transformation based on certain criteria. The criteria required is shown below.

# Problem 1: Data Cleaning
# - Load the dataset.
# - Remove rows with missing Customer ID.
# - Remove rows where Quantity <= 0.
# - Drop duplicate rows.
# - Count remaining rows and unique customers.
# Problem 2: Calculated Fields
# - Create a TotalPrice column = Quantity * UnitPrice.
# - Extract month from InvoiceDate as InvoiceMonth.
# - Calculate total revenue (TotalPrice sum).
# Problem 3: Customer RFM
# - Use snapshot date = 1 day after the last InvoiceDate.
# - Calculate for each Customer ID:
# - Recency (days since last purchase)
# - Frequency (unique invoices)
# - Monetary (total spend)
# - Sort by Monetary descending.
# Problem 4: Product Pareto (from the Pareto Principle, the 80/20 rule, i.e 80% of effects come from 20% of causes)
# - Group by Description and sum TotalPrice.
# - Sort by revenue descending.
# - Calculate cumulative % contribution to revenue.
# - Find:
# - Top 10 products by revenue
# - Number of products that make up top 80% of revenue
# Problem 5: Time-Series
# - Group by InvoiceMonth and sum TotalPrice.
# - Plot monthly revenue as a line chart.
# - Identify month with highest revenue.

import pandas as pd
from pathlib import Path

# Load CSV transformed original dataset
initial_data = pd.read_csv("../../outputs/csv/online_retail_II_combined.csv", encoding="utf-8")
# Write out HTML representation of original dataset
html_data = initial_data.head(1000).to_html(index=False, border=0, justify="left", na_rep="")
Path("../../outputs/html/tw1-original.html").write_text(html_data, encoding="utf-8")
# Evaluate stage 1 size of dataset
print("Stage 1 Dataset size (Rows Columns) - " + str(initial_data.shape))
# Remove rows where Customer ID is missing
initial_data = initial_data.dropna(subset=["Customer ID"])
# Remove rows where Quantity is less than or equal to 0
initial_data = initial_data[initial_data["Quantity"] > 0]
# Evaluate stage 2 size of dataset
print("Stage 2 Dataset size (Rows Columns) - " + str(initial_data.shape))
# Drop duplicate rows
initial_data = initial_data.drop_duplicates()
# Write out HTML representation of current dataset
html_data = initial_data.head(1000).to_html(index=False, border=0, justify="left", na_rep="")
Path("../../outputs/html/tw1-cleaned.html").write_text(html_data, encoding="utf-8")
# Evaluate stage 3 size of dataset
print("Stage 3 Dataset size (Rows Columns) - " + str(initial_data.shape))
