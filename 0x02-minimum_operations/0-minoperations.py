#usr/bin/python3
"""minimum number of operations to reach n"""
def minOperations(n):
    if n == 1:
        return 0
    operations = 0
    H = 1
    while H < n:
        if n % H == 0:
            operations += 2
            H *= 2
        else:
            H += H
            operations += 1
    return operations if H == n else 0
