import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Generate a sample dataset
np.random.seed(42)
data = np.random.normal(50, 15, 1000)  # A sample data set with mean=50 and std deviation=15

# Convert data to a DataFrame for better handling
df = pd.DataFrame(data, columns=['Values'])

# Function to calculate basic statistics
def calculate_statistics(data):
    statistics = {
        "Mean": np.mean(data),
        "Median": np.median(data),
        "Mode": stats.mode(data)[0][0],
        "Variance": np.var(data),
        "Standard Deviation": np.std(data)
    }
    return statistics

# Calculate and print statistics
statistics = calculate_statistics(df['Values'])
print("Basic Statistics:")
for key, value in statistics.items():
    print(f"{key}: {value}")

# Visualizations
def visualize_data(data):
    plt.figure(figsize=(14, 8))

    # Histogram and KDE (Kernel Density Estimation) plot
    plt.subplot(1, 2, 1)
    sns.histplot(data, kde=True, color='skyblue')
    plt.axvline(statistics['Mean'], color='red', linestyle='--', label=f"Mean: {statistics['Mean']:.2f}")
    plt.axvline(statistics['Median'], color='green', linestyle='--', label=f"Median: {statistics['Median']:.2f}")
    plt.title("Distribution with Mean and Median")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.legend()

    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(data, color='orange')
    plt.title("Box Plot of Values")
    plt.xlabel("Values")

    plt.suptitle("Statistical Data Visualization", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Call visualization function
visualize_data(df['Values'])
