# cis129_dylanMccallum_Lab05.py
"""
Module 5 Lab-5
Dylan McCallum
06/19/2024

The Bottle Return Program

This program demonstrates utilizing condition controlled loops by replicating
a bottle tracking system used by a grocery store.

"""
# declaring local variables 

counter = 1     # controls the inner loop

total_bottles = 0       # stores total bottles
today_bottles = 0       # number of bottles returned on a day
total_payout = 0        # stores calculated value of total_bottles
keep_going = 'y'        # restarts the program

while keep_going == 'y':
    
    while counter < 8:
        today_bottles = int(input(f"Enter number of bottles for day #{counter}: "))
        total_bottles += today_bottles
        total_payout = total_bottles * .10
        counter += 1
        
        
    
    print(f"\nThe total number of bottles collected is {total_bottles}")
    print(f"The total paid out is ${total_payout:.2f}")
    
    print("\nDo you want to enter another week's worth of data?")
    print("(Enter y or n)")
    
    keep_going = str(input())
    
    # resets variables to initial set values for another week's input
    if keep_going == 'y':
        
        counter = 1
        total_bottles = 0
        today_bottles = 0
        total_payout = 0