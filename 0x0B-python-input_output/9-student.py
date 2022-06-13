#!/usr/bin/python3
"""
This module creates a class student with defined attributes.
"""


class Student:
    """
    This class is defining the attributes for the student class
    Public instance attributes: first_name, last_name, age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of the attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Function that retrieves a dictionary representation of a
        Student instance.
        """
        return (self.__dict__)
