import matplotlib.pyplot as plt
import numpy as np

# Generate random data (heights of 250 people)
heights = np.random.normal(170, 10, 250)

# Plot histogram
plt.hist(heights, bins=10, edgecolor='black')  # Adjust bins for clarity
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.title('Height Distribution of 250 People')
plt.grid(True)
plt.show()
