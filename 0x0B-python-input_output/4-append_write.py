#!/usr/bin/python3
"""4_append_write"""


def append_write(filename="", text=""):
    """append_write function"""
    with open(filename, "a") as f:
        return f.write(text)
