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


# Declaring main function

def main():
    print("Main function running")
    
    deposit_system(check_one)

# Declaring function to receive monetary input

def deposit_system(cash_amt):
    print(f"we received a check in the amount of ${cash_amt:.2f}")

main()