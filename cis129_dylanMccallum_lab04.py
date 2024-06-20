# cis129_dylanMcCallum_lab04.py
"""
Module 4 Lab-4
Dylan McCallum
06/15/2024

This program calculates and determines the store's and employee's bonus
based on the amount of monthly sales generated and the sales increase
percentage.

"""

# Local variables that stores the dollar amount and percentage rate

monthlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0
prompt = 'How many sales were processed this month? '

# This code gets monthly sales from the user input 

monthlySales = float(input(prompt))

# These statements determine store's bonus based on monthly sales

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount

# This code determines the percent of increase based on sales

salesIncrease = float(input('Rate of sales increased by '))
salesIncrease = salesIncrease / 100

# This code determines the employee bonus

if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# This code outputs the store and employee bonus

print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)

# Outputs a message if maximum bonus criteria is met

if (storeAmount == 6000 and empAmount == 75):
    print("Congrats! You reached the highest bonus amounts possible!")
