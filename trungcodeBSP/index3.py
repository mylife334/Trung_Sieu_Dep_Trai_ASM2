import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the new CSV file
file_path = 'Book1.csv'
data = pd.read_csv(file_path)

# Take the first 50 rows for the regression analysis
data_50 = data.head(50)

# Prepare the data for Linear Regression
# Assume we are predicting TotalAmount based on Quantity
# We will remove rows where Quantity or TotalAmount is NaN
data_50 = data_50.dropna(subset=['Quantity', 'TotalAmount'])

X = data_50[['Quantity']].values
y = data_50['TotalAmount'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting using the model
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Calculate performance metrics
mse_train = mean_squared_error(y_train, y_pred_train)
r2_train = r2_score(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
r2_test = r2_score(y_test, y_pred_test)

# Plotting the results for training data
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='Actual (Training)')
plt.plot(X_train, y_pred_train, color='red', label='Predicted (Training)')
plt.title('Linear Regression: Quantity vs. Total Amount (Training Data)')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.legend()
plt.show()

# Plotting the results for testing data
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='green', label='Actual (Testing)')
plt.plot(X_test, y_pred_test, color='orange', label='Predicted (Testing)')
plt.title('Linear Regression: Quantity vs. Total Amount (Testing Data)')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.legend()
plt.show()

print(f"MSE (Training): {mse_train}")
print(f"R^2 (Training): {r2_train}")
print(f"MSE (Testing): {mse_test}")
print(f"R^2 (Testing): {r2_test}")
