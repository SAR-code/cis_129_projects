# cis129_lab02_coffeeShop.py
"""A Coffee shop simulator that calculates a receipt

of total items purchased and cost to the user.
"""

    


def my_coffee_shop():
    welcome_msg = '\nMy Coffee and Muffin Shop'
    receipt_msg = '\nMy Coffee and Muffin Shop Receipt'
    
    border = '**********************************'
    
    
    print( border, welcome_msg )
    
    coffee_count = int(input('Number of coffees bought? \n'))
    muffin_count = int(input('Number of muffins bought? \n'))
    
    print(border)
    
    coffee_price = 5*float(coffee_count)
    muffin_price = 4*float(muffin_count)
    
    sales_tax = (coffee_price + muffin_price) * .06
    item_total = (coffee_price + muffin_price) + sales_tax    
    
    print( border, receipt_msg )
    
    
    print(f"{coffee_count} Coffee at $5 each:", f"${coffee_price}", 
                f"\n{muffin_count} Muffins at $4 each:", f"${muffin_price}",
                f"\n6% tax: ${sales_tax} \n-------", '\nTotal:',
                f"${item_total}")
    
    
    print( border )
    


my_coffee_shop()
