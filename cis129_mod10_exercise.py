# cis129_mod10_exercise.py
"""
Module 10 exercise 8.1
Dylan McCallum
07/11/2024

The Check Protection Program

This program takes the dollar amount input then prints the amount in a
check-protected format

"""

import math

# Declaring global variables for testing

check_one = 5654.45
check_two = 1230.60
check_three = 399.87

border = "----------"
position_num = '0123456789'


# Declaring main function

def main():
    print("Main function running")
    
    deposit_system(check_two)


# Declaring function to receive monetary input

def deposit_system(cash_amt):
    
    
    cash_amt_to_string = str("{0:.2f}".format(cash_amt))
    mark = '*'
    result = ''
    
    if len(cash_amt_to_string) < 10:
        mark_calc = (10 - len(cash_amt_to_string))
        mark = mark * mark_calc
        result = mark + cash_amt_to_string
             
    print(f"{result}\n{border}\n{position_num}")

main()