import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample dataset
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Initialize logistic regression model
logr = LogisticRegression()

# Fit the model
logr.fit(X, y)

# Predict for a new data point
new_tumor_size = 3.46
predicted = logr.predict(np.array([new_tumor_size]).reshape(-1, 1))

# Convert log-odds to odds and probabilities
log_odds = logr.coef_ * new_tumor_size + logr.intercept_
odds = np.exp(log_odds)
probability = odds / (1 + odds)

# Output
print(f"Predicted class for tumor size {new_tumor_size} cm: {'Cancerous' if predicted[0] == 1 else 'Non-cancerous'}")
print(f"Probability of tumor being cancerous: {probability[0][0]:.2%}")
