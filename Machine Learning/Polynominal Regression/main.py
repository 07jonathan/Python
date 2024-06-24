import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Data
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# Fitting polynomial regression model
mymodel = np.poly1d(np.polyfit(x, y, 3))

# Generate smooth line for the curve
myline = np.linspace(1, 22, 100)

# Plot original data and polynomial regression line
plt.scatter(x, y)
plt.plot(myline, mymodel(myline), color='red')
plt.xlabel('Hour of the day')
plt.ylabel('Car speed')
plt.title('Polynomial Regression of Car Speed Over Hours')
plt.grid(True)
plt.show()

# Calculate R-squared value
r2 = r2_score(y, mymodel(x))
print(f"R-squared value: {r2:.2f}")

# Predict the speed at 17:00 (hour 17)
speed_at_17 = mymodel(17)
print(f"Predicted speed at 17:00: {speed_at_17:.2f}")
