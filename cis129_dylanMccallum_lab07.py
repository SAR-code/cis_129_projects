# cis129_dylanMccallum_lab07.py
"""
Module 7
Dylan McCallum
06/29/2024

This program contains lab 7-3 which simulates a dice game.

"""
# importing required libraries

import random

# the main function

def main():
    print()
    
    # initialize variables
    
    end_program = 'no'
    
    player_one = 'NO NAME'
    player_two = 'NO NAME'
    
    
    # call to inputName
    
    player_one, player_two = input_names(player_one, player_two)
    
    # while loop to run program again
    
    while end_program == 'no':
        
        # populate variables
        
        winners_name = 'NO NAME'
        
        p1_number = 0
        p2_number = 0
        
        # call to roll_dice
        
        winners_name = roll_dice(p1_number, p2_number, player_one, player_two)
        
        # call to display_info
        
        display_info(winners_name)
        
        end_program = input('Do you want to end program? (yes/no): ')
    
# this function get the players names

def input_names(player_1, player_2):
    
    
    return player_1, player_2
    
# this function gets the random values
def roll_dice(p1_num, p2_num, player_one, player_two):
    
    p1_num = random.randint(1, 6)
    p2_num = random.randint(1, 6)
    
    #if (p1_num == p2_num):
        
# this function displays the winner

def display_info(winners_name):
    print(winners_name)

# calls main
main()


