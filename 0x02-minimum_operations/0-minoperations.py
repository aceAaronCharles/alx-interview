#!/usr/bin/python3

"""Minimum number of operations to reach n"""


def minOperations(n):
    """Calculate minimum number of operations to reach n"""
    if n < 2:
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops if n == 1 else 0
