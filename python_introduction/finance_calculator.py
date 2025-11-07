
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}.")
# Assuming an annual interest rate of 5%
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

