#!/usr/bin/python3
"""3_write_file"""


def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, "w") as f:
        return f.write(text)
