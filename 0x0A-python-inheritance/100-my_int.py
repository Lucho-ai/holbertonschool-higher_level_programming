#!/usr/bin/python3
"""MODULE 100"""


class MyInt(int):
    """MyInt Class"""
    def __eq__(self, other):
        """eq magic method"""
        return False

    def __ne__(self, other):
        """ne magic method"""
        return True
