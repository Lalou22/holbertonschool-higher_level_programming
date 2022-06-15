#!/usr/bin/python3
"""
Function that adds 2 integers a and b must be integers or floats,
otherwise raise a TypeError exception with the message a must be an
integer or b must be an integer. a and b must be first casted to integers
if they are float.
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers. a and b must be integers or floats,
    otherwise raise a TypeError exception with the message a must be an
    integer or b must be an integer
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    elif isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
