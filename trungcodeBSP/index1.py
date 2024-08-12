import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'Book1.csv'
data = pd.read_csv(file_path)

# Convert SaleDate to datetime format
data['SaleDate'] = pd.to_datetime(data['SaleDate'])

# Fill NaN values in Quantity và TotalAmount với 0 for plotting purposes
data['Quantity'].fillna(0, inplace=True)
data['TotalAmount'].fillna(0, inplace=True)

# Take first 20 rows of the data
data_20 = data.head(20)

# 1. Bar Chart - Total Quantity Sold Each Day for first 20 entries
quantity_per_day_20 = data_20.groupby(data_20['SaleDate'].dt.date)['Quantity'].sum()
plt.figure(figsize=(10, 6))
quantity_per_day_20.plot(kind='bar', color='skyblue')
plt.title('Total Quantity Sold Each Day (First 20 Entries)')
plt.xlabel('Date')
plt.ylabel('Total Quantity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Line Chart - Total Revenue Each Day for first 20 entries
revenue_per_day_20 = data_20.groupby(data_20['SaleDate'].dt.date)['TotalAmount'].sum()
plt.figure(figsize=(10, 6))
revenue_per_day_20.plot(kind='line', marker='o', linestyle='-', color='green')
plt.title('Total Revenue Each Day (First 20 Entries)')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Pie Chart - Distribution of Payment Methods for first 20 entries
payment_method_distribution_20 = data_20['PaymentMethod'].value_counts()
plt.figure(figsize=(8, 8))
payment_method_distribution_20.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'lightgreen'])
plt.title('Distribution of Payment Methods (First 20 Entries)')
plt.ylabel('')
plt.show()
