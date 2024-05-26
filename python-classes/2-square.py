#!/usr/bin/python3
"""
a Square class that defines a square
"""


class Square:
    """Square class that define a square with is self size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """instance attribute"""
        self.__size = size
