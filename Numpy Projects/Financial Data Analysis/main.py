import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/AMZN_data_1999_2022.csv'
data = pd.read_csv(file_path, parse_dates=['Date'])

# Sort data by date for accurate calculations
data = data.sort_values('Date')

# Calculate daily returns
data['Daily Return'] = data['Close'].pct_change()

# Calculate moving averages (10-day and 50-day)
data['10-Day MA'] = data['Close'].rolling(window=10).mean()
data['50-Day MA'] = data['Close'].rolling(window=50).mean()

# Plot the stock closing price and moving averages
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Close'], label='Closing Price', color='blue')
plt.plot(data['Date'], data['10-Day MA'], label='10-Day Moving Average', color='orange')
plt.plot(data['Date'], data['50-Day MA'], label='50-Day Moving Average', color='green')
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.title('Amazon Stock Price with Moving Averages')
plt.legend()
plt.show()

# Plot daily returns distribution
plt.figure(figsize=(10, 5))
plt.hist(data['Daily Return'].dropna(), bins=50, color='purple', alpha=0.6)
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.title('Distribution of Daily Returns')
plt.show()

# Basic summary statistics
print("Summary Statistics for Amazon Stock:")
print(data[['Close', 'Daily Return', '10-Day MA', '50-Day MA']].describe())
