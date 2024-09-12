## Projects Title : Sales Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Read the sales data CSV file (Replace 'sales_data.csv' with your real-time data file)
file_path = 'sales_data.csv'
sales_data = pd.read_csv(file_path)

# Show the first few rows of the dataset
print("Sales Data Preview:")
print(sales_data.head())

# Convert 'Date' column to datetime format
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Basic Analysis
# 1. Total Sales
total_sales = sales_data['Sales'].sum()
print(f"\nTotal Sales: ${total_sales}")

# 2. Average Sales Per Product
avg_sales_per_product = sales_data.groupby('Product')['Sales'].mean()
print("\nAverage Sales per Product:")
print(avg_sales_per_product)

# 3. Monthly Sales Trend
sales_data['Month'] = sales_data['Date'].dt.to_period('M')
monthly_sales = sales_data.groupby('Month')['Sales'].sum()

# Plotting Monthly Sales Trend
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# 4. Sales by Region
sales_by_region = sales_data.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(sales_by_region)

# 5. Best Selling Product
best_selling_product = sales_data.groupby('Product')['Sales'].sum().idxmax()
print(f"\nBest Selling Product: {best_selling_product}")

# 6. Sales by Product over Time
sales_product_time = sales_data.groupby(['Product', 'Month'])['Sales'].sum().unstack()
sales_product_time.plot(kind='line', figsize=(10, 5))
plt.title('Sales by Product Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend(title='Product')
plt.xticks(rotation=45)
plt.show()
