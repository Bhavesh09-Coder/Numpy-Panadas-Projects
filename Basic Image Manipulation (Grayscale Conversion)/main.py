import numpy as np

# Project Title: Basic Image Manipulation

# Example image as a NumPy array (3x3 pixel image with RGB channels)
image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                  [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
                  [[0, 0, 0], [127, 127, 127], [255, 255, 255]]])

# Convert to grayscale using average of RGB channels
grayscale = np.mean(image, axis=2)

# Print the grayscale image
print("Grayscale Image:\n", grayscale)
