## Project title : Student Grade Analysis

df = pd.read_csv('Studgrade.csv')

# Display basic statistics
print("Basic Statistics:")
print(df['Grade'].describe())

# Calculate the average grade
average_grade = df['Grade'].mean()
print(f"\nAverage Grade: {average_grade:.2f}")

# Find the highest grade
highest_grade = df['Grade'].max()
print(f"Highest Grade: {highest_grade}")

# Calculate the grade distribution
grade_distribution = df['Grade'].value_counts().sort_index()
print(f"\nGrade Distribution:\n{grade_distribution}")

# Calculate median and mode
median_grade = df['Grade'].median()
mode_grade = df['Grade'].mode().tolist()
print(f"\nMedian Grade: {median_grade}")
print(f"Mode Grade(s): {mode_grade}")

# Visualization: Histogram of Grades
plt.figure(figsize=(10, 6))
sns.histplot(df['Grade'], bins=10, kde=True, color='skyblue')
plt.title('Distribution of Student Grades')
plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Visualization: Boxplot of Grades
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Grade'], color='lightcoral')
plt.title('Boxplot of Student Grades')
plt.xlabel('Grade')
plt.grid(True)
plt.show()
