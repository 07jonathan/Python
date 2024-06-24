import numpy as np

def calculate_standard_deviation(speed_values):
    """Calculate and print the standard deviation of a list of speed values."""
    std_dev = np.std(speed_values)
    mean_value = np.mean(speed_values)
    print(f"Speed values: {speed_values}")
    print(f"Mean value: {mean_value}")
    print(f"Standard deviation: {std_dev}")
    print()

# Example 1
speed1 = [86, 87, 88, 86, 87, 85, 86]
calculate_standard_deviation(speed1)

# Example 2
speed2 = [32, 111, 138, 28, 59, 77, 97]
calculate_standard_deviation(speed2)
