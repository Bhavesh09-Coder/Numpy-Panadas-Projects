# Project Title: Array Element-wise Operations

import numpy as np

# Define two example arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

# Element-wise addition
addition_result = np.add(array1, array2)

# Element-wise subtraction
subtraction_result = np.subtract(array1, array2)

# Element-wise multiplication
multiplication_result = np.multiply(array1, array2)

# Element-wise division
division_result = np.divide(array1, array2)

# Display results
print("Array 1:", array1)
print("Array 2:", array2)
print("Element-wise Addition:", addition_result)
print("Element-wise Subtraction:", subtraction_result)
print("Element-wise Multiplication:", multiplication_result)
print("Element-wise Division:", division_result)
