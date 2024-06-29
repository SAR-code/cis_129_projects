# cis129_lab06_hotdog_cookout.py
"""
Module 6 Lab-6
Dylan McCallum
06/22/2024

Hotdog Cookout Program

This program calculates the number of hotdogs and the number of buns required
for a cookout with the minimum amount of leftover ingredients. Program will
request basic information from the user on the number of guest attending the
cookout and the amount of hotdogs each person is given.

"""

import math     # importing math module

# declaring global variable for total hotdogs

total_hotdogs = 0

# declaring function to get the total number of hotdogs

def get_total_hotdogs():
    
    # declaring local variables for calculations
    
    attendees = 0   # number of people attending
    hotdogs = 0     # number of hotdogs per person
    
    # receiving user input on number of attendees and hotdogs
    
    attendees = int(input("Maximum amount of people attending?: "))
    hotdogs = int(input("How many hotdogs per attendee?: "))
    
    # calculates the total between hotdogs and attendees
    
    total = attendees * hotdogs
    
    return total    # returns the total

# reassigning global variable to a function

total_hotdogs = get_total_hotdogs()

# declaring function to get results of remaining hotdogs and buns leftover

def show_results(total):
    
    # initializing required constants to simulate packaging
    
    DOGS = 10
    BUNS = 8
    
    # declaring local variables for leftover items
    
    dogs_left = 0
    buns_left = 0
    
    # declaring local variables for minimum required items
    
    min_dogs = 0
    min_buns = 0
    
    # calculating the minimum items required and the leftover ingredients
    
    dogs_left = (DOGS - total % DOGS) % DOGS
    min_dogs = (total / DOGS) + (0**(0** dogs_left))
    
    buns_left = (BUNS - total % BUNS) % BUNS
    min_buns = (total / BUNS) + (0**(0** buns_left))
    
    # displays message to the user
    
    print(f"\nMinimum packages of hotdogs needed: {math.floor(min_dogs)}",
           f"\nHotdogs remaining: {dogs_left}")
    
    print(f"\nMinimum packages of hotdog buns needed: {math.floor(min_buns)}",
           f"\nHotdog buns remaining: {buns_left}")

# invokes function to display results

show_results(total_hotdogs)

