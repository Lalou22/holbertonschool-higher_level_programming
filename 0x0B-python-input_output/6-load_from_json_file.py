#!/usr/bin/python3
import json
"""
This module contains a function that creates an Object from a “JSON file”.
"""


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”.
    """
    with open(filename) as myFile:
        new_obj = json.load(myFile)
    return (new_obj)
