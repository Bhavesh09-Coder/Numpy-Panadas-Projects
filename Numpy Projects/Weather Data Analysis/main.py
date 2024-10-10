# weather_analysis.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the weather data
data = pd.read_csv('weather_data.csv')

# Convert the 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Display the first few rows of the dataset
print("Weather Data:")
print(data.head())

# Calculate basic statistics
mean_temp = np.mean(data['Temperature (°C)'])
max_temp = np.max(data['Temperature (°C)'])
min_temp = np.min(data['Temperature (°C)'])
mean_humidity = np.mean(data['Humidity (%)'])

print("\nStatistics:")
print(f"Mean Temperature: {mean_temp:.2f} °C")
print(f"Max Temperature: {max_temp:.2f} °C")
print(f"Min Temperature: {min_temp:.2f} °C")
print(f"Mean Humidity: {mean_humidity:.2f} %")

# Create a line plot for Temperature
plt.figure(figsize=(14, 6))
sns.lineplot(x=data['Date'], y=data['Temperature (°C)'], marker='o', label='Temperature (°C)')
sns.lineplot(x=data['Date'], y=data['Humidity (%)'], marker='o', label='Humidity (%)')

# Adding title and labels
plt.title('Weather Data Analysis')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
