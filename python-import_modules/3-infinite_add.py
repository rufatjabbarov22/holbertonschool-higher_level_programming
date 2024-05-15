#!/usr/bin/python3
import sys

if __name__ == "__main__":
    from sys import argv

    args = sys.argv[1:]
    addition = 0

    for numbers in args:
        addition += int(numbers)

    print(addition)
