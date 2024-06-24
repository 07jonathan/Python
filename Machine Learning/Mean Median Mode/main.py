import numpy as np
from scipy import stats

# List of speeds
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Calculate Mean
mean_speed = np.mean(speed)
print(f"Mean: {mean_speed}")

# Calculate Median
median_speed = np.median(speed)
print(f"Median: {median_speed}")

# Calculate Mode
mode_speed = stats.mode(speed)
print(f"Mode: {mode_speed.mode[0]}")
