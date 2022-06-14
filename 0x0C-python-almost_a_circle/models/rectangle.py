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
        Setter receives and validates value as param.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        Setter receives and validates value as param.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        Setter receives and validates value as param.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        Setter receives and validates value as param.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Public method that returns the area value of the instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Public method that prints in stdout the Rectangle instance with
        the character # - you don’t need to handle x and y here.
        """
        print("\n".join(("#" * self.__width) for a in range(self.__height)))
