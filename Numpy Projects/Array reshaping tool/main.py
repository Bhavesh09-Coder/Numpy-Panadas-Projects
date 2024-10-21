import numpy as np

def reshape_array(arr, dimensions):
    """
    Function to reshape a 1D array into a 2D or 3D array based on user input dimensions.
    
    :param arr: Input 1D array
    :param dimensions: Tuple representing the new shape (e.g., (2, 3) for 2D, (2, 2, 3) for 3D)
    :return: Reshaped array
    """
    try:
        reshaped_arr = np.reshape(arr, dimensions)
        return reshaped_arr
    except ValueError:
        print(f"Cannot reshape array of size {arr.size} into shape {dimensions}")
        return None

def main():
    # Sample 1D array
    arr = np.arange(1, 13)  # Create an array with values 1 to 12
    print(f"Original 1D array:\n{arr}\n")

    # Get user input for dimensions
    dimension_type = input("Enter '2D' to reshape into 2D array or '3D' for 3D array: ").strip().upper()

    if dimension_type == '2D':
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        dimensions = (rows, cols)
    elif dimension_type == '3D':
        depth = int(input("Enter the number of layers (depth): "))
        rows = int(input("Enter the number of rows per layer: "))
        cols = int(input("Enter the number of columns per layer: "))
        dimensions = (depth, rows, cols)
    else:
        print("Invalid input. Please enter '2D' or '3D'.")
        return

    reshaped = reshape_array(arr, dimensions)

    if reshaped is not None:
        print(f"\nReshaped array ({dimension_type}):\n{reshaped}")

if __name__ == "__main__":
    main()
