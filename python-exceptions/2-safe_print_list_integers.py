#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    calculate, idx = 0, 0

    while idx < x:
        try:
            print("{:d}".format(my_list[idx]), end="")
            calculate += 1
        except (TypeError, ValueError):
            pass
        idx += 1

    print()
    return calculate
