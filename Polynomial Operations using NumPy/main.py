import numpy as np

# Define two polynomials as NumPy arrays
# Example: 2x^2 + 3x + 4 is represented as [2, 3, 4]
poly1 = np.array([2, 3, 4])
poly2 = np.array([1, -2, 3])

# Polynomial Addition
poly_add = np.polyadd(poly1, poly2)

# Polynomial Subtraction
poly_sub = np.polysub(poly1, poly2)

# Polynomial Multiplication
poly_mul = np.polymul(poly1, poly2)

# Display the results
print("Polynomial 1:", np.poly1d(poly1))
print("Polynomial 2:", np.poly1d(poly2))
print("\nAddition Result:", np.poly1d(poly_add))
print("Subtraction Result:", np.poly1d(poly_sub))
print("Multiplication Result:", np.poly1d(poly_mul))
