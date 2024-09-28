import pandas as pd

# Load the dataset
file_path = '/mnt/data/customer_data.csv'
data = pd.read_csv(filepath)

# Calculate the average purchase value
data['AvgPurchaseValue'] = data['TotalAmountSpent'] / data['TotalPurchases']

# Summary statistics
age_distribution = data['Age'].describe()

# Count of customers by gender
gender_distribution = data['Gender'].value_counts()

# Count of customers by location
location_distribution = data['Location'].value_counts()

# Grouped statistics for average purchase value by age and gender
avg_purchase_by_age_gender = data.groupby(['Age', 'Gender'])['AvgPurchaseValue'].mean().reset_index()

# Total amount spent by location
total_amount_by_location = data.groupby('Location')['TotalAmountSpent'].sum().reset_index()

# Churn Rate (assuming low frequency = potential churn)
# Define churn based on purchase frequency (this can be customized)
# For simplicity, let's assume customers with < 10 purchases are potential churners
churn_data = data.copy()
churn_data['Churn'] = churn_data['TotalPurchases'] < 10
churn_rate = churn_data['Churn'].mean() * 100  # Percentage of customers likely to churn

# Customer loyalty (high frequency = loyal customers)
loyalty_data = churn_data[~churn_data['Churn']].copy()
loyalty_rate = len(loyalty_data) / len(churn_data) * 100

# Print or return the analysis results as needed
{
    "age_distribution": age_distribution,
    "gender_distribution": gender_distribution,
    "location_distribution": location_distribution,
    "avg_purchase_by_age_gender": avg_purchase_by_age_gender,
    "total_amount_by_location": total_amount_by_location,
    "churn_rate": churn_rate,
    "loyalty_rate": loyalty_rate
}

