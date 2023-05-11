#!/usr/bin/python3
""" Module that reads stdin line """

import sys

status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
output = 0


def main():
    """ Method that prints stdin line by line """
    print("File size: {}".format(output))
    for status in sorted(status_code.keys()):
        if status_code[status]:
            print("{}: {}".format(status, status_code[status]))


if __name__ == '__main__':
    count = 0
    try:
        for line in sys.stdin:
            try:
                words = line.split()
                output += int(words[-1])
                if words[-2] in status_code:
                    status_code[words[-2]] += 1
            except:
                pass
            if count == 9:
                main()
                count = -1
            count += 1
    except KeyboardInterrupt:
        main()
        raise
    main()
