#!/usr/bin/python3
"""
This module contains a function that returns the number
of lines of a text file.
"""


def number_of_lines(filename=""):
    nb_lines = 0
    """
    This function returns the number of lines of a text file.
    Must use the with statement, don’t need to manage file
    permission or file doesn't exist exceptions and 
    not allowed to import any module
    """
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            nb_lines += 1
    return (nb_lines)
