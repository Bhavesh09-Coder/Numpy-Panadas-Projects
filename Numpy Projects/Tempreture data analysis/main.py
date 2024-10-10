# Project Title: Temperature Data Analysis

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the temperature data
data = pd.read_csv('temperature_data.csv')

# Convert the 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Display the first few rows of the dataset
print("Temperature Data:")
print(data.head())

# Calculate basic statistics
mean_temp = np.mean(data['Temperature (°C)'])
max_temp = np.max(data['Temperature (°C)'])
min_temp = np.min(data['Temperature (°C)'])
median_temp = np.median(data['Temperature (°C)'])
std_temp = np.std(data['Temperature (°C)'])

print("\nStatistics:")
print(f"Mean Temperature: {mean_temp:.2f} °C")
print(f"Max Temperature: {max_temp:.2f} °C")
print(f"Min Temperature: {min_temp:.2f} °C")
print(f"Median Temperature: {median_temp:.2f} °C")
print(f"Standard Deviation: {std_temp:.2f} °C")

# Create a line plot for Temperature
plt.figure(figsize=(14, 6))
sns.lineplot(x=data['Date'], y=data['Temperature (°C)'], marker='o')

# Adding title and labels
plt.title('Temperature Data Analysis')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
