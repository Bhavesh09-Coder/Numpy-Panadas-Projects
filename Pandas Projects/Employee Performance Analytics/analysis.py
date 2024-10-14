import pandas as pd

def analyze_performance(df):
    # Data Cleaning
    df_cleaned = df.dropna()  # Remove rows with missing values
    
    # Handle duplicates if present
    df_cleaned = df_cleaned.drop_duplicates()
    
    # Filtering irrelevant columns
    if 'Employee_ID' in df_cleaned.columns:
        df_cleaned = df_cleaned.drop(columns=['Employee_ID'])  # Drop unnecessary ID column if present
    
    # Analysis: Generating Performance Metrics
    average_satisfaction = df_cleaned['satisfaction_level'].mean()
    average_evaluation = df_cleaned['last_evaluation'].mean()
    average_projects = df_cleaned['number_project'].mean()
    turnover_rate = (df_cleaned['left'].mean()) * 100  # Percentage of employees who left
    
    # Create a performance report
    report = {
        "Average Satisfaction Level": average_satisfaction,
        "Average Last Evaluation Score": average_evaluation,
        "Average Number of Projects": average_projects,
        "Employee Turnover Rate (%)": turnover_rate
    }

    return df_cleaned, report
