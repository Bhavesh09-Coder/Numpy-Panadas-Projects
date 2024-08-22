import numpy as np
import matplotlib.pyplot as plt

# Example data points
data_points = np.random.normal(loc=0, scale=1, size=1000)

# Generate histogram
hist, bins = np.histogram(data_points, bins=30)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(data_points, bins=bins, color='blue', alpha=0.7)
plt.title("Histogram of Data Points")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
