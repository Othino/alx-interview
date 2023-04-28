#!/usr/bin/python3
"""
Pascal's Triangle
"""


def binomialCoeff(n, k):
    """ calculate the value of Binomial Coefficient """
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def pascal_triangle(n):
    """
    Returns  list of lists of integers representing
    the Pascal’s triangle of n or an empty list if n <= 0
    You can assume n will be always an integer
    """
    l1 = []
    for line in range(0, n):
        l2 = []
        for i in range(0, line + 1):
            l2.append(binomialCoeff(line, i))
        l1.append(l2)
    return l1
