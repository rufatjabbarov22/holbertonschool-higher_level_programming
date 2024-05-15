#!/usr/bin/python3

a = 10
b = 5

from calculator_1 import add, sub, mul, div

print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
