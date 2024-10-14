import seaborn as sns
import matplotlib.pyplot as plt

def visualize_performance(df):
    # Histogram for Satisfaction Levels
    plt.figure(figsize=(10, 6))
    sns.histplot(df['satisfaction_level'], kde=True)
    plt.title('Distribution of Employee Satisfaction Levels')
    plt.xlabel('Satisfaction Level')
    plt.ylabel('Frequency')
    plt.show()

    # Bar chart for Employee Turnover by Department
    plt.figure(figsize=(10, 6))
    sns.countplot(x='department', hue='left', data=df)
    plt.title('Employee Turnover by Department')
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')
    plt.xticks(rotation=45)
    plt.legend(title="Left Company", loc="upper right")
    plt.show()

    # Scatter Plot: Satisfaction Level vs. Last Evaluation
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='satisfaction_level', y='last_evaluation', hue='left', data=df)
    plt.title('Satisfaction Level vs. Last Evaluation')
    plt.xlabel('Satisfaction Level')
    plt.ylabel('Last Evaluation Score')
    plt.legend(title="Left Company", loc="upper right")
    plt.show()

    # Box plot for Average Monthly Hours by Department
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='department', y='average_montly_hours', data=df)
    plt.title('Average Monthly Hours by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Monthly Hours')
    plt.xticks(rotation=45)
    plt.show()
