monthly_income = int(input("Enter your monthly income: "))

total_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = int(monthly_income - total_monthly_expenses)

project_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")

print(f"Projected savings after one year, with interest, is: ${project_savings}.")
