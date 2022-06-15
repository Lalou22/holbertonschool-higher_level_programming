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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation of list_objs
        to a file. list_objs is a list of instances who inherits of Base.
        If list_objs is None, save an empty list.
        """
        _file = cls.__name__ + ".json"
        _list = []
        if list_objs is not None:
            for i in list_objs:
                _list.append(cls.to_dictionary(i))
        with open(_file, "w") as myFile:
            myFile.write(cls.to_json_string(_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON string representation.
        If json_string is None or empty, return an empty list.
        Otherwise, return the list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))
