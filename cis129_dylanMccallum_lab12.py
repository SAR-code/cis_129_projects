# cis129_dylanMccallum_lab12.py
"""
Module 12 
Dylan McCallum
07/28/2024

This program demonstrates OOP principles utilizing a pet class object
as an example with validation.

"""

"""Class Pet with read-write properties."""

class Pet:
    """Class Pet with read-write properties."""
    
    def __init__(self, name=str, type=str, age=int):
        """Initialize each attribute."""
        
        self.name = name        # pet name
        self.type = type        # type of pet
        self.age = age          # pet age
    
    def __repr__(self):
        """Returns string representation."""
        
        return f"A {self.type} named {self.name} whose {self.age} years old"
    
    @property
    def name(self):
        """Returns the name of the pet."""
        
        return self._name
    
    @name.setter
    def name(self, name):
        """Sets the pet name."""
        
        self._name = name    
    
    @property
    def type(self):
        """Returns the pet type."""
        
        return self._type
    
    @type.setter
    def type(self, type):
        """Sets the pet type."""
        
        self._type = type
    
    @property
    def age(self):
        """Returns the pet age."""
        
        return self._age 
    
    @age.setter
    def age(self, age):
        """Sets the pet age."""
        
        self._age = age


# declare main function to hold program operations

def main():
    
    # declare local variables
    
    is_valid = False
    
    # resets the loop if incorrect input is detected
    
    while is_valid == False:
        
        try:
            
            # wrap user input into variables
            
            pet_name = str(input("Enter your pet's name: ")).title()

            # validates for letters only input
            
            if not pet_name.isalpha():
                print("Invalid input, only letters")
                continue
            
            pet_type = str(input("Enter your pet's type: ")).lower()
            
            # validates for letters only input
            
            if not pet_type.isalpha():
                print("Invalid input, only letters")
                continue
            
            pet_age = int(input(f"{pet_name}'s age: "))
            
            # validates age input for negative numbers
            
            if pet_age < 0:
                print("Can't be negative years")
                continue
        
        except ValueError:
            print("You must enter a number for age")
        else:
            
            # inputs variables into the function as arguments
            
            pet_info(pet_name, pet_type, pet_age)
            
            # ends the while loop upon correct input
            
            is_valid = True
    

# declare function to accept user input to use as arguments for constructor

def pet_info(p_name=str, p_type=str, p_age=int):
    
    # creates a new instance of a pet
    
    new_pet = Pet(p_name, p_type, p_age)
    
    # outputs the various information regarding the pet created
    
    print(f"\nThe pet name is {new_pet.name}")
    print(f"\nThe pet type is {new_pet.type}")
    print(f"\nThe pet age is {new_pet.age}")

# invokes main function

main()