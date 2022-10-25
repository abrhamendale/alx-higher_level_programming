#!/usr/bin/python3
"""Append_write"""


def append_write(filename="", text=""):
    """Appends text to a file."""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
