# cis129_mod11_exercise_9_1.py
"""
Module 11 exercise 9.1
Dylan McCallum
07/21/2024

Writing Grades To A Plain Text File

This program calculates grades from the class and returns the class average
and then stores the grades in a text file.

"""
# declare main function to hold program operations

def main():
    print("Hello")
    
    # create a grades.txt to write and store grades into
    with open('grades.txt', mode='w') as grades:
        grades.write('100 Dylan 98\n')
        grades.write('200 Alex 79\n')
        grades.write('300 Dan 84\n')
        

# invokes main function

main()