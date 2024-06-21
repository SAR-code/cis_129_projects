# cis129_dylanMccallum_Lab05.py
"""
Module 5 Lab-5
Dylan McCallum
06/19/2024

The Bottle Return Program

This program demonstrates utilizing condition controlled loops by replicating
a bottle tracking system used by a grocery store.

"""
# declaring local variables for bottle return program 

counter = 1             # controls the inner loop

total_bottles = 0       # stores total bottles
today_bottles = 0       # stores number of bottles returned on a day
total_payout = 0        # stores calculated value of total_bottles

keep_going = 'y'        # restarts the program

# outer while-loop starts the program

while keep_going == 'y':
    
    # nested inner-loop takes the user's input for bottles entered
    
    while counter < 8:
        
        # takes the number of bottles from the user
        
        today_bottles = int(
            input(f"Enter number of bottles for day #{counter}: ")
        )
        
        # calculates total bottles and payout amount
        
        total_bottles += today_bottles      
        total_payout = total_bottles * .10
        
        counter += 1    # counter updates after each iteration until day 7
        
        
    # This code displays total bottles collected and final calculations
    
    print(f"\nThe total number of bottles collected is {total_bottles}")
    print(f"The total paid out is ${total_payout:.2f}")
    
    # prompts the user on whether or not to enter additional data
    
    print("\nDo you want to enter another week's worth of data?")
    
    # determines whether to continue or break the loop based on user's input
    
    keep_going = str(input("(Enter y or n): "))
    
    # resets variables to the initial set values for another week's input

    if keep_going == 'y':
        
        counter = 1
        total_bottles = 0
        today_bottles = 0
        total_payout = 0