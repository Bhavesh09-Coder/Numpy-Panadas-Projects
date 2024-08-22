# Project Title: Polynomial Operations

import numpy as np

# Define two polynomials (e.g., 2x^2 + 3x + 4 and x^2 + 2x + 1)
poly1 = np.array([2, 3, 4])  # Coefficients for 2x^2 + 3x + 4
poly2 = np.array([1, 2, 1])  # Coefficients for x^2 + 2x + 1

# Perform polynomial addition, subtraction, and multiplication
poly_add = np.polyadd(poly1, poly2)
poly_sub = np.polysub(poly1, poly2)
poly_mul = np.polymul(poly1, poly2)

# Display the results
print(f"Addition Result: {np.poly1d(poly_add)}")
print(f"Subtraction Result: {np.poly1d(poly_sub)}")
print(f"Multiplication Result: {np.poly1d(poly_mul)}")
