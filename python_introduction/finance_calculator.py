monthlyIncome = int(input("Enter your monthly income: "))
totalMonthlyExpenses = int(input("Enter your total monthly expenses: "))

monthlySavings = monthlyIncome - totalMonthlyExpenses

# Assumptions
# 1. Simple annual interest rate of 5%
projectedSavings = int(monthlySavings * 12 + (monthlySavings * 12 * 0.05))

print(f"Your monthly savings are ${monthlySavings}")
print(f"Projected savings afer one year, with interest is: ${projectedSavings}.")
