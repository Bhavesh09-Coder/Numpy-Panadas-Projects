import pandas as pd

# Load the employee dataset
file_path = '/mnt/data/employees_data.csv'
df = pd.read_csv(file_path)

# Data Preprocessing
# Check for missing values and handle them
df.isnull().sum()

# Filling missing values for age with the median age (can adjust based on context)
df['Age'].fillna(df['Age'].median(), inplace=True)

# Check for incorrect or missing gender values and standardize them
df['Gender'] = df['Gender'].str.capitalize().replace({'M': 'Male', 'F': 'Female'})
df['Gender'].fillna('Unknown', inplace=True)

# Generate new analysis columns if needed (e.g., for location analysis)
# Assuming there is a location column, it can be cleaned or adjusted similarly if applicable

# Analyze salary distribution across job titles
salary_by_job_title = df.groupby('Job Title')['Salary'].describe()

# Analyze gender distribution
gender_distribution = df['Gender'].value_counts()

# Analyze age distribution
age_distribution = df['Age'].describe()

# Correlation between salary and age, salary and gender (dummy encoded)
df['Gender_encoded'] = df['Gender'].map({'Male': 1, 'Female': 0})
correlation_salary_age = df[['Salary', 'Age']].corr()
correlation_salary_gender = df[['Salary', 'Gender_encoded']].corr()

# Return or print analysis results for further review
{
    "salary_by_job_title": salary_by_job_title,
    "gender_distribution": gender_distribution,
    "age_distribution": age_distribution,
    "correlation_salary_age": correlation_salary_age,
    "correlation_salary_gender": correlation_salary_gender
}
