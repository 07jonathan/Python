import matplotlib.pyplot as plt
import numpy as np

# Data
categories = np.array(["A", "B", "C", "D"])
values = np.array([3, 8, 1, 10])

# Vertical Bar Graph
plt.figure(figsize=(8, 6))  # Optional: adjust figure size
plt.bar(categories, values, color="skyblue", width=0.5)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Vertical Bar Graph')
plt.grid(True)  # Optional: add grid lines
plt.show()

# Horizontal Bar Graph
plt.figure(figsize=(8, 6))  # Optional: adjust figure size
plt.barh(categories, values, color="lightgreen", height=0.5)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Graph')
plt.grid(True)  # Optional: add grid lines
plt.show()
