import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# 1. Plot Age Distribution
def plot_age_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Age'], bins=10, kde=True, color='blue')
    plt.title('Distribution of Customers by Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

# 2. Plot Gender Distribution
def plot_gender_distribution(data):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=data, x='Gender', palette='Set2')
    plt.title('Distribution of Customers by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()

# 3. Plot Location Distribution
def plot_location_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Location', palette='Set1')
    plt.title('Distribution of Customers by Location')
    plt.xlabel('Location')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# 4. Plot Average Purchase Value by Age and Gender
def plot_avg_purchase_by_age_gender(avg_purchase_by_age_gender):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=avg_purchase_by_age_gender, x='Age', y='AvgPurchaseValue', hue='Gender', marker='o', palette='Set1')
    plt.title('Average Purchase Value by Age and Gender')
    plt.xlabel('Age')
    plt.ylabel('Average Purchase Value ($)')
    plt.show()

# 5. Plot Total Purchase Amount by Location
def plot_total_amount_by_location(total_amount_by_location):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=total_amount_by_location, x='Location', y='TotalAmountSpent', estimator=sum, palette='Set3')
    plt.title('Total Purchase Amount by Location')
    plt.xlabel('Location')
    plt.ylabel('Total Amount Spent ($)')
    plt.xticks(rotation=45)
    plt.show()

# Call the plot functions after passing the necessary analysis data

# plot_age_distribution(data)
# plot_gender_distribution(data)
# plot_location_distribution(data)
# plot_avg_purchase_by_age_gender(avg_purchase_by_age_gender)
# plot_total_amount_by_location(total_amount_by_location)
