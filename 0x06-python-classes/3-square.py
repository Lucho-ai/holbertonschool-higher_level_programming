#!/usr/bin/python3
class Square:
    """Basic square class #3"""

    def __init__(self, size=0):
        """Initialize square"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Calculates square area"""
        return self.__size ** 2
