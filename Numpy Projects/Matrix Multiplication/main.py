# Project Title: Matrix Multiplication using NumPy

import numpy as np

# Function to multiply two matrices
def matrix_multiplication(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# Example matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Perform matrix multiplication
result = matrix_multiplication(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResult of Matrix Multiplication:")
print(result)
