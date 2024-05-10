#!/usr/bin/python3

output = ""

for num in range(100):
    output += "{:02d}".format(num)
    if num < 99:
        output += ", "

print(output)
