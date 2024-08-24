# Project Title: Array Reshaping

import numpy as np

def reshape_array(arr, new_shape):
    """Function to reshape a NumPy array to a new shape."""
    try:
        reshaped_array = arr.reshape(new_shape)
        return reshaped_array
    except ValueError as e:
        return str(e)

# Create a 1D NumPy array
array_1d = np.arange(12)  # Array with 12 elements

# Reshape the array to 2D
array_2d = reshape_array(array_1d, (3, 4))

# Reshape the array to 3D
array_3d = reshape_array(array_1d, (2, 2, 3))

print("Original 1D Array:", array_1d)
print("Reshaped to 2D Array:\n", array_2d)
print("Reshaped to 3D Array:\n", array_3d)
