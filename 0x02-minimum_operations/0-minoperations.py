#!/usr/bin/python3
""" Module that calculates operations """


def minOperations(n):
    """
    Method that calculates the fewest number of
    operations needed
    """
    if n < 2 or type(n) is not int:
        return 0
    check = []
    val = n
    i = 1
    while val != 1:
        i += 1
        if val % i == 0:
            while (val % i == 0 and val != 1):
                val = val / i
                check.append(i)
    return sum(check)
