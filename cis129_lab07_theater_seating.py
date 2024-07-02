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
    
    # welcome, styling, and info message variables
    
    welcome_message = 'Welcome to our Drama Theatre!\n'
    border = '**********************************'
    
    print(border)
    
    
    print(welcome_message,
                f"\nWe charge ${TICKET_A} for section {SECTION_LIST[0]}.",
                f"\nWe charge ${TICKET_B} for section {SECTION_LIST[1]}.",
                f"\nWe charge ${TICKET_C} for section {SECTION_LIST[2]}.\n",
        )
    
    print(border)
    
    ticket_sales = get_tickets(SECTION_LIST)

    print(border)
    
    total_sales = calculate_theater_sales(ticket_sales, TICKET_A, 
                                          TICKET_B, TICKET_C
                                          )
    
    print(border)
   
    print(f"\nTotal ticket revenue: ${total_sales[0]}"
          f"\nTotal seats sold: {total_sales[1]}")
    
    print(border)


def calculate_theater_sales(ticket_sales, sec_a, sec_b, sec_c):
    
    price_per_section = 0
    total_sales = 0
    total_seats = 0
    
    
    for section, number_tickets in ticket_sales:
        if section == "A":
            price_per_section = number_tickets * sec_a
            total_sales += number_tickets * sec_a
            total_seats += number_tickets
            print(f"\nSection {section} subtotal: ${price_per_section}, seats: {number_tickets}")
        elif section == 'B':
            price_per_section = number_tickets * sec_b
            total_sales += number_tickets * sec_b
            total_seats += number_tickets
            print(f"\nSection {section} subtotal: ${price_per_section}, seats: {number_tickets}")
        elif section == 'C':
            price_per_section = number_tickets * sec_c
            total_sales += number_tickets * sec_c
            total_seats += number_tickets
            print(f"\nSection {section} subtotal: ${price_per_section}, seats: {number_tickets}")
            
    return total_sales, total_seats

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