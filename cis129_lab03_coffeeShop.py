# cis129_lab02_coffeeShop.py
"""
A Coffee shop function that calculates a receipt
of total items purchased and cost to the user.

"""


def my_coffee_shop():
    """Variables containing various messages and styling."""
    
    welcome_msg = '\nMy Coffee and Bakery Shop'
    receipt_msg = '\nMy Coffee and Bakery Shop Receipt'
    thank_msg = '\nThank you for stopping by!'
    shameless_plug = '\nCheck our social media!\nMenu items change monthly!'
    
    border = '**********************************' 
    print(border, welcome_msg)
    
    """Variables converting str to int to receive number inputs."""
    
    coffee_count = int(input('Number of coffees bought? \n'))
    muffin_count = int(input('Number of muffins bought? \n'))
    
    """New items added to the menu."""
    
    water_count = int(input("Number of bottled water bought? \n"))
    cinnamon_roll_count = int(input("Number of cinnamon rolls bought? \n"))
    
    print(border)
    
    """Calculates total number of items with final price and tax."""
    
    coffee_price = 5 * float(coffee_count)
    muffin_price = 4 * float(muffin_count)
    bottled_water_price = 2 * float(water_count)
    cinnamon_roll_price = 3 * float(cinnamon_roll_count)
    
    sales_tax = (coffee_price 
                 + muffin_price 
                 + bottled_water_price 
                 + cinnamon_roll_price) * .06
    
    item_total = (coffee_price 
                  + muffin_price 
                  + bottled_water_price 
                  + cinnamon_roll_price) + sales_tax    
    
    """Outputs receipt message with final item count and purchase."""
    
    print(border, receipt_msg)
    
    print(f"{coffee_count} Coffee at $5 each:", f"${coffee_price:.2f}" 
                ,f"\n{muffin_count} Muffins at $4 each:" 
                ,f"${muffin_price:.2f}"
                ,f"\n{water_count} Bottled Water at $2 each:"
                ,f"${bottled_water_price:.2f}"
                ,f"\n{cinnamon_roll_count} Cinnamon Rolls at $3 each:"
                ,f"${cinnamon_roll_price:.2f}"
                ,f"\n6% tax: ${sales_tax} \n-------", '\nTotal:'
                ,f"${item_total}")
    
    print(thank_msg, shameless_plug)
    print(border)

my_coffee_shop()
