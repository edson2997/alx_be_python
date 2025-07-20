monthly_income = float (input( "Enter your monthly income:"))
total_monthly_expenses = float (input ("Enter your total monthly expenses:"))
# Calculate the monthly savings by subtracting monthly expenses from the monthly income.
monthly_savings = monthly_income - total_monthly_expenses
# Assume a simple annual interest rate of 5%.
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are {}".format(monthly_savings))
print ("Projected savings after one year, with interest, is:{}".format(projected_savings))



