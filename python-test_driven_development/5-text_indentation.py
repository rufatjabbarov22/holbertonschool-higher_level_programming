#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    current_line = ""
    for char in text:
        if char is " " and char is text[0] and current_line is " ":
            current_line = "\n"
            continue
        if char is " " and current_line is "\n":
            continue
        if char is "." or char is "?" or char is ":":
            print(char)
            print()
            current_line = "\n"
        else:
            print(char, end="")
            current_line = char
