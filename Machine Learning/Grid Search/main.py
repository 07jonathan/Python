from sklearn import datasets
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Define parameter grid
param_grid = {
    'C': [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0],
    'solver': ['liblinear', 'newton-cg', 'lbfgs', 'sag', 'saga']
}

# Create logistic regression model
logit = LogisticRegression(max_iter=10000)

# Setup grid search cross-validation
grid_search = GridSearchCV(estimator=logit, param_grid=param_grid, cv=5)

# Fit grid search
grid_search.fit(X, y)

# Print best parameters and best score
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
