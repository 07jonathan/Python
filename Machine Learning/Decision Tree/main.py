import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("data.csv")

# Mapping for 'Nationality' and 'Go'
nationality_mapping = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(nationality_mapping)

go_mapping = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(go_mapping)

# Define features and target
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# Create and train Decision Tree Classifier
dtree = DecisionTreeClassifier()
dtree.fit(X, y)

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(dtree, feature_names=features, class_names=['NO', 'YES'], filled=True)
plt.show()

# Example predictions
# Prediction 1: Age=40, Experience=10, Rank=7, Nationality=USA
prediction = dtree.predict([[40, 10, 7, 1]])
if prediction[0] == 1:
    print("Suggested to attend the comedy show.")
else:
    print("Not suggested to attend the comedy show.")

# Prediction 2: Rank=6
prediction = dtree.predict([[40, 10, 6, 1]])
if prediction[0] == 1:
    print("Suggested to attend the comedy show.")
else:
    print("Not suggested to attend the comedy show.")
