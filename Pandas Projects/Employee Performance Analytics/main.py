import pandas as pd
from analysis import analyze_performance
from visualize import visualize_performance

# Load the dataset
data_path = 'employee_performance_data.csv'  # Replace with the actual dataset file path
df = pd.read_csv(data_path)

# Perform data cleaning and analysis
cleaned_data, performance_report = analyze_performance(df)

# Visualize the performance data
visualize_performance(cleaned_data)

# Output the report
print("Performance Analysis Report:")
print(performance_report)
