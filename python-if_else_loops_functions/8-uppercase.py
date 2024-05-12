#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        result += uppercase_char

    print("{}".format(result))
