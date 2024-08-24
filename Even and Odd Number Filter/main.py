# Project Title: Even and Odd Number Filter

import numpy as np

def filter_even_odd(arr):
    """Function to separate even and odd numbers from a NumPy array."""
    even_numbers = arr[arr % 2 == 0]
    odd_numbers = arr[arr % 2 != 0]
    return even_numbers, odd_numbers

# Create a NumPy array
array = np.array([10, 15, 23, 42, 55, 64, 77])

# Filter even and odd numbers
evens, odds = filter_even_odd(array)

print("Original Array:", array)
print("Even Numbers:", evens)
print("Odd Numbers:", odds)
