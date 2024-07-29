# cis129_dylanMccallum_lab12.py
"""
Module 12 
Dylan McCallum
07/28/2024

This program demonstrates OOP principles utilizing a pet class object
as an example.

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
