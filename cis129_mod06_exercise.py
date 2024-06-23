# cis129_mod06_exercise.py
"""
Module 6 Exercise
Dylan McCallum
06/22/2024

This program contains module 6 exercises as per the assignment.

"""
test_list = [1, 2, 3, 4, 5]

def cube(x):
    """Calculate the cube of x."""
    return x ** 3
print('The cube of 2 is', cube(2))

def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y

mystery(test_list)

def seconds_since_midnight(hour, minute, second):
    hour_in_seconds =  hour * 3600
    minute_in_seconds = minute * 60
    return hour_in_seconds + minute_in_seconds + second


