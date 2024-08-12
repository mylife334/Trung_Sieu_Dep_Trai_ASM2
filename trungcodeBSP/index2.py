import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'Book1.csv'
data = pd.read_csv(file_path)

# Take the first 20 rows for the regression analysis
data_20 = data.head(20)

# Prepare the data for Linear Regression
# Assume we are predicting TotalAmount based on Quantity
# We will remove rows where Quantity or TotalAmount is NaN
data_20 = data_20.dropna(subset=['Quantity', 'TotalAmount'])

X = data_20[['Quantity']].values
y = data_20['TotalAmount'].values

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predicting using the model
y_pred = model.predict(X)

# Display the coefficients
intercept = model.intercept_
coefficient = model.coef_[0]

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted')
plt.title('Linear Regression: Quantity vs. Total Amount')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.legend()
plt.show()

(intercept, coefficient)
