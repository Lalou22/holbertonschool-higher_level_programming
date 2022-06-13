#!/usr/bin/python3
"""
This module contains a function that returns the number
of lines of a text file.
"""


def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines
    """
    i = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            i += 1
            print(line, end="")
            if nb_lines == i:
                break
