import pandas as pd

# Sample dataset of employees' income statements
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "Finance", "IT", "HR", "IT"],
    "Basic_Salary": [50000, 60000, 70000, 55000, 72000],
    "Bonus": [5000, 7000, 8000, 4500, 9000],
    "Deductions": [2000, 2500, 3000, 1800, 3500]
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Calculate Total Income for each employee
df["Total_Income"] = df["Basic_Salary"] + df["Bonus"] - df["Deductions"]

# Display the dataset
print("Employee Income Statement:")
print(df)

# Analysis
total_income = df["Total_Income"].sum()
average_income = df["Total_Income"].mean()
income_by_department = df.groupby("Department")["Total_Income"].sum()

# Insights
print("\nIncome Analysis:")
print(f"Total Income of all employees: {total_income}")
print(f"Average Income of employees: {average_income:.2f}")
print("\nIncome by Department:")
print(income_by_department)

# Save the analysis to a CSV file
output_file = "employee_income_analysis.csv"
df.to_csv(output_file, index=False)
print(f"\nAnalysis saved to {output_file}")
