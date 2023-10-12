#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    Given a number n,
    write a method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
