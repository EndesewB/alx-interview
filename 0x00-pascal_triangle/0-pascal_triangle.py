#!/usr/bin/python3
"""
pascal's triangle module
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of list of int: A list of lists representing Pascal's triangle.
                            Each inner list represents a row in the triangle.
                            Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            row = [1]
        else:
            prev_row = triangle[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)

        triangle.append(row)

    return triangle
