#!/usr/bin/python3
"""2_read_lines"""


def read_lines(filename="", nb_lines=0):
    """read_lines function"""
    if type(filename) == str:
        with open(filename) as f:
            if type(nb_lines) != int:
                print(f.read(), end="")
                return
        with open(filename) as f:
            if nb_lines <= 0 or nb_lines >= len(f.readlines()):
                f.seek(0)
                print(f.read(), end="")
                return
        with open(filename) as f:
            for line in range(nb_lines):
                print(f.readline(), end="")
