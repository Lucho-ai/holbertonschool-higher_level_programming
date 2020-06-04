#!/usr/bin/python3
"""1_number_lines"""


def number_of_lines(filename=""):
    """number_of_lines function"""
    with open(filename) as f:
        return len(f.readlines())
