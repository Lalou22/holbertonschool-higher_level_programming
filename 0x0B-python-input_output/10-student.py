#!/usr/bin/python3
"""
This module creates a class student with defined attributes.
You are not allowed to import any module.
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

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary representation of
        a Student instance. If attrs is a list of strings, only attribute
        names contained in this list must be retrieved. Otherwise, all
        attributes must be retrieved.
        """
        if attrs is None:
            return (self.__dict__)
        dict_ = {}
        for a in attrs:
            try:
                dict_[a] = self.__dict__[a]
            except:
                pass
        return dict_
