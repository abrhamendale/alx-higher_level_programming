#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Checks for inheritance."""
    if a_class in type(obj).__bases__ or a_class == object:
        return (True)
    else:
        return (False)