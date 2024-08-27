# Project Title: Mean, Median, and Mode Calculator

import numpy as np
from scipy import stats

# Function to calculate mean, median, and mode
def calculate_statistics(arr):
    mean_value = np.mean(arr)
    median_value = np.median(arr)
    mode_value = stats.mode(arr)[0][0]
    
    return mean_value, median_value, mode_value

# Example array of numbers
numbers = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6])

# Calculate mean, median, and mode
mean, median, mode = calculate_statistics(numbers)

# Display the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
