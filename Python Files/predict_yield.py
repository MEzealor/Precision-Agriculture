# Import necessary libraries
from sklearn.metrics import mean_squared_error, r2_score

# Assuming the model has been trained and predictions are made
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE) and R² Score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation results
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")

# Optional: You can also print a scatter plot of actual vs predicted values for visual inspection
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)  # Diagonal line
plt.xlabel('Actual Yield')
plt.ylabel('Predicted Yield')
plt.title('Actual vs Predicted Crop Yield')
plt.show()
