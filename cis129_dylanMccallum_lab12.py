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
        """Initialize each attribute"""
        
        self.name = name        # pet name
        self.type = type        # type of pet
        self.age = age          # pet age
    
    def __repr__(self):
        return f"A {self.type} named {self.name} whose {self.age} years old"
    
    