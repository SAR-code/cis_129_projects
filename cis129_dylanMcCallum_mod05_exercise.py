# cis129_dylanMccallum_mod05_exercise.py
"""
Module 5 Exercise
Dylan McCallum
06/19/2024

This program contains module 5 exercises.

"""

passes = 0  # number of passes
failures = 0  # number of failures

correct_inputs = 0 # number of correct inputs
failed_inputs = 0 # number of failed inputs

student = 0 # number of students to process


# process 10 students
while student < 10:
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
        
    # validates the user input and tracks all failed input attempts
    if result != 1 and result != 2:
        print("Incorrect input")   
        failed_inputs = failed_inputs + 1    
    elif result == 1:   # tracks correct inputs and increments each variable
        passes = passes + 1
        correct_inputs = correct_inputs + 1
        student += 1
    else:   # tracks correct inputs and increments each variable
        failures = failures + 1
        correct_inputs = correct_inputs + 1
        student += 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)

print('Correct Inputs:', correct_inputs) 
print('Failed Inputs:', failed_inputs)

if passes > 8:
    print('Bonus to instructor')