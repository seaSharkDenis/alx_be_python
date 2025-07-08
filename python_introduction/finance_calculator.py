monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

# Assumptions
# 1. Simple annual interest rate of 5%
projectedSavings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings afer one year, with interest is: ${int(projectedSavings)}.")