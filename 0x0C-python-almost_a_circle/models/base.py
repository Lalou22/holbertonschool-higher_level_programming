#!/usr/bin/python3
"""
This modules contains a class Base
with all its methods and attributes
definition
"""


class Base:
    """
    This class has a private attribute __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of class which checks for id. If id is not None
        assign the public instance attribute id with this argument
        otherwise, increment __nb_objects and assign the new value
        to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
