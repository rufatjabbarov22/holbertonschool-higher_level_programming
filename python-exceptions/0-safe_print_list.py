#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements_printed = 0

    for idx in range(x):
        try:
            print(my_list[idx], end="")
            elements_printed += 1
        except IndexError:
            break

    print()

    return elements_printed
