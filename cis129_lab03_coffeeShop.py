# cis129_lab02_coffeeShop.py
"""A Coffee shop simulator that calculates a receipt

of total items purchased and cost to the user.
"""

    


def my_coffee_shop():
    welcome_msg = """*****Welcome My Coffee and Muffin shop*****"""
    print( welcome_msg )
    
    coffee = int(input('How many orders of coffee would you like? '))
    muffin = int(input('How many orders of muffins would you like? '))
    
    coffee_price = 5*float(coffee)
    muffin_price = 4*float(muffin)
    
    item_total = coffee_price + muffin_price
    
    print('Number of coffees bought:', coffee, 'Number of muffins bought:', muffin)
    
    print('Coffee total:', f"${coffee_price}", 'Muffin total:'
                , f"${muffin_price}", 'Item total:', f"${item_total}")
    


my_coffee_shop()
