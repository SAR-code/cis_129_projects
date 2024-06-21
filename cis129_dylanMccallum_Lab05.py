# cis129_dylanMccallum_Lab05.py
"""
Module 5 Lab-5
Dylan McCallum
06/19/2024

This program demonstrates utilizing condition controlled loops by replicating
a bottle tracking program used by a grocery store.

"""
# declaring local variables 

counter = 1     # controls the loop

total_bottles = 0       # stores total bottles
today_bottles = 0       # number of bottles returned on a day
total_payout = 0        # stores calculated value of total_bottles
keep_going = 'y'        # restarts the program

while keep_going == 'y':
    print("Do you want to enter another week's worth of data?")
    print("(Enter y or n)")
    keep_going = str(input())