#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    This is the class Rectangle containing Private instance attributes,
    each with its own public getter and setter: 
    Attributes __width,  __height, __x and __y and a class constructor.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor. Call the super class with id then Assign each
        argument width, height, x and y to the right attribute.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Returns the width.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter receives value as param.
        """
        self.__width = value

    @property
    def height(self):
        """
        Return the height.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter receives value as param.
        """
        self.__height = value

    @property
    def x(self):
        """
        Returns the x.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter receives value as param.
        """
        self.__x = value

    @property
    def y(self):
        """
        Returns the y.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter receives value as param.
        """
        self.__y = value
