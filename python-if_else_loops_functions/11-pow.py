#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        result = 1
        for _ in range(b):
            result *= a
    else:
        result = 1.0 / pow(a, -b)
    return result

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
print(pow(-98, -10))
