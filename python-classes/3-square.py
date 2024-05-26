#!/usr/bin/python3
"""
A class used to represent a Square
"""


class Square:
    """Square class that define a square with is self size"""
    def __init__(self, size=0):
        """Initialize the square with a given size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        """The area of the square"""
        return self.__size ** 2
