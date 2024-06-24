import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Read the data
df = pd.read_csv("data.csv")

# Select features (Weight and Volume) and target (CO2)
X = df[['Weight', 'Volume']]
y = df['CO2']

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the features
scaled_X = scaler.fit_transform(X)

# Initialize the Linear Regression model
regr = LinearRegression()

# Train the model
regr.fit(scaled_X, y)

# Example: Predict CO2 emission for a car with Weight=2300 kg and Volume=1.3 liters
new_data = [[2300, 1.3]]
scaled_new_data = scaler.transform(new_data)
predicted_CO2 = regr.predict(scaled_new_data)

print("Predicted CO2 emission:", predicted_CO2[0])
