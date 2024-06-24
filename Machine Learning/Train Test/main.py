import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Generate synthetic data
np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

# Split data into training and testing sets
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

# Fit a polynomial regression model
degree = 4  # degree of polynomial
model = np.poly1d(np.polyfit(train_x, train_y, degree))

# Calculate R-squared (R2) for training set
train_y_pred = model(train_x)
r2_train = r2_score(train_y, train_y_pred)
print(f"R-squared score on training set: {r2_train:.3f}")

# Calculate R-squared (R2) for testing set
test_y_pred = model(test_x)
r2_test = r2_score(test_y, test_y_pred)
print(f"R-squared score on testing set: {r2_test:.3f}")

# Plotting the results
plt.figure(figsize=(10, 5))

# Plot training data
plt.scatter(train_x, train_y, color='blue', label='Training data')

# Plot testing data
plt.scatter(test_x, test_y, color='green', label='Testing data')

# Plot the model
x_line = np.linspace(0, 6, 100)
plt.plot(x_line, model(x_line), color='red', label=f'Polynomial regression (degree {degree})')

plt.title('Polynomial Regression Fit')
plt.xlabel('Minutes before purchase')
plt.ylabel('Amount of money spent')
plt.legend()
plt.grid(True)
plt.show()

# Predicting for new value
new_value = 5
predicted_amount = model(new_value)
print(f"Predicted amount for {new_value} minutes: {predicted_amount:.2f} dollars")
