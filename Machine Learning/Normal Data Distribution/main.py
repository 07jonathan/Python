import numpy as np
import matplotlib.pyplot as plt

# Generate a dataset with 100000 values following a normal distribution
mean = 5.0
std_dev = 1.0
size = 100000
x = np.random.normal(mean, std_dev, size)

# Plot a histogram of the generated data
plt.hist(x, bins=100, density=True, alpha=0.7, color='blue')  # density=True for normalized histogram
plt.title('Normal Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
