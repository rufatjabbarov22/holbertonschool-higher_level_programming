#!/usr/bin/python3

"""Function that removes all c and C characters from a string"""


def no_c(my_string):
    return ''.join(char for char in my_string if char not in 'cC')
