# Data Normalization using NumPy

import numpy as np

# Sample dataset
data = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400],
    [250, 350, 450],
    [300, 400, 500]
])

# Function to normalize data to a range of [0, 1]
def normalize_min_max(data):
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

# Function to standardize data (mean=0, std=1)
def standardize(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std
    return standardized_data

# Normalize the data to [0, 1]
normalized_data = normalize_min_max(data)
print("Normalized Data (Min-Max Scaling):")
print(normalized_data)

# Standardize the data (Mean = 0, Standard Deviation = 1)
standardized_data = standardize(data)
print("\nStandardized Data (Mean = 0, Std Dev = 1):")
print(standardized_data)
