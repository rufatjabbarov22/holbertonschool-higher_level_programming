#!/usr/bin/python3
"""
divides all elements of a matrix

return error if:
is not int and float
is not same size
div is not int and float
div = 0
"""
def matrix_divided(matrix, div):
    """
    divide a matrix by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")


    new_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for value in row:
            m = ("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(value, (int, float)):
                raise TypeError(m)
            new_row.append(round(value / div, 2))
        new_matrix.append(new_row)
    return (new_matrix)
