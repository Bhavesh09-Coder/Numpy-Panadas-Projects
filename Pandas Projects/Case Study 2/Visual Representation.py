import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# 1. Plot the Salary Distribution by Job Title
def plot_salary_by_job_title(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Job Title', y='Salary', data=df, palette='Set3')
    plt.title('Salary Distribution by Job Title')
    plt.xlabel('Job Title')
    plt.ylabel('Salary')
    plt.xticks(rotation=45)
    plt.show()

# 2. Plot Gender Distribution
def plot_gender_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Gender', palette='Set2')
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()

# 3. Plot Age Distribution
def plot_age_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=10, kde=True, color='blue')
    plt.title('Age Distribution of Employees')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

# 4. Correlation between Salary and Age
def plot_salary_age_correlation(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Salary', data=df, hue='Gender', palette='Set1')
    plt.title('Correlation between Salary and Age')
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.show()

# Example of calling:
# plot_salary_by_job_title(df)
# plot_gender_distribution(df)
# plot_age_distribution(df)
# plot_salary_age_correlation(df)
