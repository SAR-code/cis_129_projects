# cis129_lab07_theater_seating.py
"""
Module 7
Dylan McCallum
06/30/2024

This program contains the module 7 lab theater seating program.

"""
# global validation constants

LOW_VALUE = 0

# the main function

def main():
    
    # variables for ticket price
    
    TICKET_A = 20
    TICKET_B = 15
    TICKET_C = 10
    
    # variables for section seats
    
    SECTION_LIST = ["A", "B", "C"]
    
    ticket_sales = get_tickets(SECTION_LIST)
    
    total_sales = calculate_theater_sales(ticket_sales, TICKET_A, 
                                          TICKET_B, TICKET_C
                                          )
    
    print(f"Total ticket revenue: ${total_sales}")


def calculate_theater_sales(ticket_sales, sec_a, sec_b, sec_c):
    total_sales = 0
    
    for section, number_tickets in ticket_sales:
        if section == "A":
            total_sales += number_tickets * sec_a
        elif section == 'B':
            total_sales += number_tickets * sec_b
        elif section == 'C':
            total_sales += number_tickets * sec_c
    return total_sales

def get_tickets(section_list):
    ticket_sales = []
    valid = False
    
    while valid == False:
        for section in section_list:
            tickets_sold = int(input(f"Tickets sold in section {section}: "))
            newValue = (get_valid_num(tickets_sold))
            
            if newValue < 0:
                continue
            else:
                ticket_sales.append((section, tickets_sold))
                valid = True
    return ticket_sales

def get_valid_num(str_msg):
    
    new_value = int(str_msg)
    
    while new_value < LOW_VALUE:
        print("Invalid Value")
        new_value = int(str_msg)
        raise ValueError("Cannot be negative")
        
    
    return new_value

main()