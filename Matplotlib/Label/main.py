import numpy as np
import matplotlib.pyplot as plt

# Data for the plot
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# Plotting the data
plt.plot(x, y)

# Adding a title and axis labels with customized font properties
plt.title("Sports Watch Data", loc='left', fontdict={'family': 'serif', 'color': 'blue', 'size': 20})
plt.xlabel("Average Pulse", fontdict={'family': 'serif', 'color': 'purple', 'size': 15})
plt.ylabel("Calorie Burnage", fontdict={'family': 'serif', 'color': 'purple', 'size': 15})

# Display the plot
plt.show()
