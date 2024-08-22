# Project Title: Histogram Generator

import numpy as np
import matplotlib.pyplot as plt

# Example data points
data_points = np.random.normal(0, 1, 1000)  # Generate 1000 random data points

# Generate histogram
plt.hist(data_points, bins=30, edgecolor='black')

# Add titles and labels
plt.title("Histogram of Data Points")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Display the histogram
plt.show()
