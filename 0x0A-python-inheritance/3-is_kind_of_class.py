#!/usr/bin/python3
"""Inheritance module"""


def is_kind_of_class(obj, a_class):
    """Checks if it is an instance of the class."""
    if type(obj) is a_class or isinstance(obj, a_class):
        return (True)
    else:
        return (False)
