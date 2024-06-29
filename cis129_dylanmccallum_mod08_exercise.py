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
# declaring global variables with mixed casing, regex, and spacing for testing

test_string1 = ' Ra D /ar ! @' 
test_string2 = 'bobca!t@'
test_string3 = 'rac[]ec#ar'
test_string4 = '!pine_apple'

# declaring function to determine whether a string is a palindrome

def is_palindrome(str):
    
    # variable containing regex
    
    punctuation = '''/!()-[]{};:'",<>./?@#$%^&*_~'''  
    
    # Removes punctuations and space using a for-loop and if-statement
    
    for punc in str:
        if punc in punctuation:
            str = str.replace(punc, "")
    
    # initializes a new list that ignores case sensitivity and spaces
    
    stack = [str.lower().replace(" ","")]
    
    # reverse the string inside the stack
    
    stack_reversed = stack[0] [::-1]
    
    # compares the original stack with the string reversed stack
    
    if stack[0] == stack_reversed:
        
        #if output is True
        
        print(f"{stack} is a palindrome!")
        return True
    else: 
        
        #if output is False
        
        print(f"I'm sorry, {stack} is not a palindrome")
        return False

# invokes the function and determines whether the function is True or False

isBool = is_palindrome(test_string1)

if (isBool):
    print("True")
else:
    print('False')