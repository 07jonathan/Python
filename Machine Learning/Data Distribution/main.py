import numpy as np
import matplotlib.pyplot as plt

# Generate 250 random floats between 0 and 5
x_small = np.random.uniform(0.0, 5.0, 250)

# Plot histogram for the small dataset
plt.figure(figsize=(8, 6))
plt.hist(x_small, bins=5, edgecolor='black')
plt.title('Histogram of 250 Random Numbers between 0 and 5')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Generate 100000 random floats between 0 and 5
x_large = np.random.uniform(0.0, 5.0, 100000)

# Plot histogram for the large dataset
plt.figure(figsize=(8, 6))
plt.hist(x_large, bins=100, edgecolor='black')
plt.title('Histogram of 100000 Random Numbers between 0 and 5')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
