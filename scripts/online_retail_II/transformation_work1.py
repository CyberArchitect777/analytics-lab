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

