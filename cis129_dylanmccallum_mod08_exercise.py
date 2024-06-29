# cis129_dylanmccallum_mod08_exercise.py
"""
Module 8, Exercise 5.9
Dylan McCallum
06/28/2024

This program contains module 8 exercise 5.9 as per the assignment.

"""

"""
    Code snippet for 5.9
    (PALINDROME TESTER)
    
    A function that takes a string and returns True if the given word is a
    palindrome, and False otherwise.
    
"""
# declaring global variable as a test string with mixed casing

test_string1 = ' Ra D /ar ! @' 
test_string2 = 'bobca!t@'

# declaring function to determine whether a string is a palindrome

def is_palindrome(str):
    
    # initializing a stack to hold the string value
    
    #stack = []
    
    # variable containing regex
    
    punctuation = '''/!()-[]{};:'",<>./?@#$%^&*_~'''  
    
    # Removes punctuations and space using a for-loop and if-statement
    
    for punc in str:
        if punc in punctuation:
            str = str.replace(punc, "")
    
    # converts string to lowercase and replaces/removes spaces
    
    stack = [str.lower().replace(" ","")]
    
    stack_reversed = stack[0] [::-1]
    
    if stack[0] == stack_reversed:
        print(f"{stack} is a palindrome!")
    else: 
        print(f"I'm sorry, {stack} is not a palindrome")
        


is_palindrome(test_string1)