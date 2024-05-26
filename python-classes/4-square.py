#!/usr/bin/python3
"""
A class used to represent a Square
"""


class Square:
    """Square class that define a square with is self size"""
    def __init__(self, size=0):
        self.size = size
    """Initialize the square with a given size"""
    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
