import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Display first few rows
print("=== Original Data ===")
print(df.head())

# Data Cleaning
# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Convert data types if needed
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

print("\n=== Cleaned Data ===")
print(df.head())

# Filtering
high_sales = df[df['Sales'] > 10000]

print("\n=== Products with Sales > 10000 ===")
print(high_sales)

# Grouping
category_summary = df.groupby('Category').agg({
    'Sales': 'sum',
    'Quantity': 'sum'
}).reset_index()

print("\n=== Category Summary ===")
print(category_summary)

# Summary Statistics
print("\n=== Summary Statistics ===")
print(df.describe())

# Insights
top_category = category_summary.loc[
    category_summary['Sales'].idxmax(), 'Category'
]

print(f"\nTop Performing Category: {top_category}")

# Graph
plt.figure(figsize=(8,5))
plt.bar(category_summary['Category'],
        category_summary['Sales'])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()