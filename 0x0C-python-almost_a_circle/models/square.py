#!/usr/bin/python3
"""
This module contains the class Square that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class contains instantiation of the class Square
    that inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height.
        The width and height must be assigned to the value of size.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloading __str__ method should return [Square]
        (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))
