# cis129_mod10_exercise.py
"""
Module 10 exercise 8.1
Dylan McCallum
07/11/2024

The Check Protection Program

This program takes the dollar amount input then prints the amount in a
check-protected format with leading asterisks

"""

# Declaring global variables for testing
# variables for different check monetary amounts

check_one = 315654.45
check_two = 1230.60
check_three = 399.87
check_four = 8.20
check_five = 47.98
large_check = 7760000.00

# output code to mirror styling results

border = "----------"
position_num = '0123456789'

# Declaring main function

def main():

    # invokes deposit function

    deposit_system(check_three)

# Declaring function to receive monetary input

def deposit_system(cash_amt):

    # initializing local variables for string conversion and placeholders

    cash_amt_to_string = str("{0:.2f}".format(cash_amt))
    mark = '*'
    result = ''

    # determines how many asterisks to input based on checks character count

    if len(cash_amt_to_string) < 10:

        # determines the difference between the position nums and check input

        mark_calc = (10 - len(cash_amt_to_string))

        # asterisks are multiplied by the difference

        mark = mark * mark_calc

        # applies the number of asterisks based on check amount

        result = mark + cash_amt_to_string

        # displays the correct format for the check, border, and position numbers

        print(f"{result}\n{border}\n{position_num}")
    else:
        # if the check exceeds position numbers

        print("That's a large check, please consult your bank!")

# invokes main function

main()