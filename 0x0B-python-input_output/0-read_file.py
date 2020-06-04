#!/usr/bin/python3
"""0_read_file"""


def read_file(filename=""):
    """read_file function"""
    with open(filename) as f:
        print(f.read(), end="")
