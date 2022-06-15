#!/usr/bin/python3
"""
This modules contains a class Base
with all its methods and attributes
definition
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation of
        list_dictionaries. If list_dictionaries is None or empty, return
        the string: "[]". Otherwise, return the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
