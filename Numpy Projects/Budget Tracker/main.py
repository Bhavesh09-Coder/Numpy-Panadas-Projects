import numpy as np
import csv

# Function to read CSV data for expenses and incomes
def read_csv_data(file_name):
    data = []
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                data.append(float(row[1]))
    except FileNotFoundError:
        print(f"{file_name} not found. Please ensure the file exists.")
    return np.array(data)

# Function to calculate total income, expenses, and savings
def calculate_budget(income_data, expense_data):
    total_income = np.sum(income_data)
    total_expenses = np.sum(expense_data)
    savings = total_income - total_expenses
    
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Savings: {savings}")
    
    analyze_spending(expense_data)

# Function to analyze spending habits
def analyze_spending(expenses):
    categories = ["Rent", "Groceries", "Transportation", "Entertainment", "Utilities"]
    total_expense = np.sum(expenses)
    
    for i, category in enumerate(categories):
        category_expense = expenses[i]
        percentage = (category_expense / total_expense) * 100
        print(f"{category}: {category_expense} ({percentage:.2f}% of total expenses)")

# Main function to execute the budget tracker
def main():
    income_data = read_csv_data('income.csv')
    expense_data = read_csv_data('expenses.csv')
    
    if len(income_data) > 0 and len(expense_data) > 0:
        calculate_budget(income_data, expense_data)

if __name__ == "__main__":
    main()
