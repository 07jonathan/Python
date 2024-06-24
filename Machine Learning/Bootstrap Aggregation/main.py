# Import necessary libraries
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

# Load the wine dataset from sklearn
data = datasets.load_wine(as_frame=True)
X = data.data
y = data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=22)

# Evaluate performance of a single Decision Tree Classifier (base classifier)
dtree = DecisionTreeClassifier(random_state=22)
dtree.fit(X_train, y_train)

y_pred_dt = dtree.predict(X_test)

print("Single Decision Tree Classifier Performance:")
print("Test data accuracy:", accuracy_score(y_true=y_test, y_pred=y_pred_dt))
print()

# Create a range of values for number of estimators (base classifiers in Bagging)
estimator_range = [2, 4, 6, 8, 10, 12, 14, 16]

models = []
scores = []

# Iterate over different number of estimators
for n_estimators in estimator_range:
    # Create Bagging Classifier
    clf = BaggingClassifier(base_estimator=DecisionTreeClassifier(random_state=22),
                            n_estimators=n_estimators,
                            random_state=22)
    
    # Fit the model
    clf.fit(X_train, y_train)
    
    # Predict on test set
    y_pred_bagging = clf.predict(X_test)
    
    # Calculate accuracy score
    score = accuracy_score(y_true=y_test, y_pred=y_pred_bagging)
    
    # Store model and score
    models.append(clf)
    scores.append(score)
    
    print(f"Bagging Classifier with {n_estimators} estimators:")
    print(f"Test data accuracy: {score}")
    print()

# Plotting results
plt.figure(figsize=(9, 6))
plt.plot(estimator_range, scores, marker='o')
plt.title('Accuracy vs. Number of Estimators in Bagging Classifier')
plt.xlabel('Number of Estimators')
plt.ylabel('Accuracy')
plt.xticks(estimator_range)
plt.grid(True)
plt.show()
