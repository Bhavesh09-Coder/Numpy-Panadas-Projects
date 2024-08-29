# Project Title: Data Normalization

import numpy as np

# Define a dataset (array)
data = np.array([10, 20, 30, 40, 50])

# Normalize the dataset to have a mean of 0 and standard deviation of 1
normalized_data = (data - np.mean(data)) / np.std(data)

# Display results
print("Original Data:", data)
print("Normalized Data:", normalized_data)
