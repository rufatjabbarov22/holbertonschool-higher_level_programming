#!/usr/bin/python3

a = 1
b = 2

from add_0 import add as FAKE_add

result = FAKE_add(a, b)

print("{} + {} = {}".format(a, b, result))

