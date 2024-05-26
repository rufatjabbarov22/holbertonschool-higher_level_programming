#!/usr/bin/python3
"""
A class used to represent a Square
"""


class Square:
    """A class used to represent a Square.

    Attributes
    size : (int): The size of one side of the square.
    position : tuple of 2 ints : The position offset for printing the square.

    Methods
    area(): Returns the area of the square.
    my_print(): Prints the square with the character '#'.
    """
    def __init__(self, size=0, position=(0, 0)):
        """"Initialize the square with a given size and position"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(val, int) for val in value) or \
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#'.
        If the size of the square is 0, prints an empty line. The position
        offset is considered when printing the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
