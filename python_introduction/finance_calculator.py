monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Ensure monthly_savings is calculated as monthly_income - total_monthly_expenses
monthly_savings = monthly_income - total_monthly_expenses
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${project_savings:.2f}.")
