#!/usr/bin/python3

'''
    quick doc
'''


def pascal_triangle(n):
    '''
        quick doc
    '''

    if n <= 0:
        return []

    triangle = []
    prev = []
    for row_len in range(1, n + 1):
        row = [1]
        for idx in range(1, row_len):
            if idx == row_len - 1:
                row.append(1)
            else:
                num = prev[idx - 1] + prev[idx]
                row.append(num)
        prev = row
        triangle.append(row)

    return triangle
