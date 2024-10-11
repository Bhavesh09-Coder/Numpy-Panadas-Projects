import pandas as pd

#### Load the dataset
file_path = '/mnt/data/country_wise_latest.csv'
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Data Summary:")
print(df.info())
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check for any missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Basic statistical summary of numerical columns
print("\nStatistical summary of numerical data:")
print(df.describe())

#### Data Cleaning & Transforming


# Dropping columns that may not be relevant for our analysis
columns_to_drop = ['WHO Region']  # Adjust based on your dataset
df_cleaned = df.drop(columns=columns_to_drop)

# Handle missing values (you could choose to fill with 0 or drop)
df_cleaned.fillna(0, inplace=True)

# Add new metrics (example: Active Cases = Total Cases - Recovered - Deaths)
df_cleaned['Active Cases'] = df_cleaned['Confirmed'] - df_cleaned['Recovered'] - df_cleaned['Deaths']

# Add a Recovery Rate column
df_cleaned['Recovery Rate'] = (df_cleaned['Recovered'] / df_cleaned['Confirmed']) * 100

# Add a Mortality Rate column
df_cleaned['Mortality Rate'] = (df_cleaned['Deaths'] / df_cleaned['Confirmed']) * 100

# Display cleaned data
print("\nCleaned dataset preview:")
print(df_cleaned.head())


#### Data Analysis

# Total Cases Worldwide
total_cases = df_cleaned['Confirmed'].sum()

# Total Recoveries Worldwide
total_recoveries = df_cleaned['Recovered'].sum()

# Total Deaths Worldwide
total_deaths = df_cleaned['Deaths'].sum()

# Global Recovery and Mortality Rates
global_recovery_rate = (total_recoveries / total_cases) * 100
global_mortality_rate = (total_deaths / total_cases) * 100

print("\n--- Global Statistics ---")
print(f"Total Confirmed Cases: {total_cases}")
print(f"Total Recovered: {total_recoveries}")
print(f"Total Deaths: {total_deaths}")
print(f"Global Recovery Rate: {global_recovery_rate:.2f}%")
print(f"Global Mortality Rate: {global_mortality_rate:.2f}%")

