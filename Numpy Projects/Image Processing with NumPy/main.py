import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load and convert the image to a NumPy array
def load_image(image_path):
    img = Image.open(image_path)
    return np.array(img)

# Save NumPy array as an image
def save_image(np_array, save_path):
    img = Image.fromarray(np_array)
    img.save(save_path)

# Flip image horizontally or vertically
def flip_image(image_array, axis):
    """ Flip the image along specified axis: 0 for vertical, 1 for horizontal """
    return np.flip(image_array, axis)

# Rotate image by 90, 180, or 270 degrees
def rotate_image(image_array, degrees):
    """ Rotate the image by the specified degrees (90, 180, 270) """
    if degrees == 90:
        return np.rot90(image_array)
    elif degrees == 180:
        return np.rot90(image_array, 2)
    elif degrees == 270:
        return np.rot90(image_array, 3)
    else:
        raise ValueError("Rotation degree must be 90, 180, or 270")

# Change color channels (e.g., swap red and blue)
def change_color_channels(image_array, channel_order):
    """ Rearrange color channels. For RGB, the order can be [2, 1, 0] to swap R and B """
    return image_array[:, :, channel_order]

# Display original and processed images
def display_images(original, processed, title):
    plt.figure(figsize=(10, 5))
    
    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")
    
    # Processed image
    plt.subplot(1, 2, 2)
    plt.imshow(processed)
    plt.title(title)
    plt.axis("off")
    
    plt.show()

# Load image
image_path = 'your_image_path.jpg'  # Replace with your image path
image_array = load_image(image_path)

# 1. Flip image horizontally
flipped_image = flip_image(image_array, axis=1)
display_images(image_array, flipped_image, "Horizontally Flipped Image")

# 2. Rotate image by 90 degrees
rotated_image = rotate_image(image_array, degrees=90)
display_images(image_array, rotated_image, "90 Degree Rotated Image")

# 3. Change color channels to swap red and blue
color_changed_image = change_color_channels(image_array, [2, 1, 0])
display_images(image_array, color_changed_image, "Color Channels Swapped (RGB to BGR)")

# Save processed image
save_image(color_changed_image, 'processed_image.jpg')
