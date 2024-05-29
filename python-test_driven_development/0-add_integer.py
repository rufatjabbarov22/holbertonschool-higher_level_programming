#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Return the addition of two integer

    a (int, float) the first number
    b (int, float) the second number default is 98
    Computes the sum of two integers
        return error if a or b is not integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
