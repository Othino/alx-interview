#!/usr/bin/python3
""" Module to determine whether a given data is valid UTF-8 """


def validUTF8(data):
    """
    Method that determines given a set of data
    represents a valid UTF-8 encoding and returns
    True: if data is a valid UTF-8 enconding
    False: if not
    """

    nbytes = 0

    m1 = 1 << 7
    m2 = 1 << 6

    for i in data:
        m = 1 << 7
        if nbytes == 0:
            while m & i:
                nbytes += 1
                m = m >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (i & m1 and not (i & m2)):
                return False
        nbytes -= 1
    return nbytes == 0
