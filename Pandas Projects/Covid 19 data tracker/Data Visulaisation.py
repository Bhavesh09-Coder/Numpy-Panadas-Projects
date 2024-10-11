### Plot 1: Top 10 Countries by Confirmed Cases

import seaborn as sns
import matplotlib.pyplot as plt

# Select top 10 countries by confirmed cases
top_10_confirmed = df_cleaned.nlargest(10, 'Confirmed')

# Bar plot for Confirmed Cases
plt.figure(figsize=(10, 6))
sns.barplot(x='Country/Region', y='Confirmed', data=top_10_confirmed)
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xticks(rotation=45)
plt.show()

### Plot 2: Recovery Rate vs Mortality Rate

# Scatter plot for Recovery Rate vs Mortality Rate
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Recovery Rate', y='Mortality Rate', hue='Country/Region', data=top_10_confirmed)
plt.title("Recovery Rate vs Mortality Rate (Top 10 Countries)")
plt.show()

### Plot 3: Heatmap of COVID-19 Statistics

# Correlation matrix
plt.figure(figsize=(10, 8))
correlation_matrix = df_cleaned[['Confirmed', 'Recovered', 'Deaths', 'Active Cases']].corr()

# Heatmap to visualize correlations
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Heatmap of COVID-19 Statistics")
plt.show()
