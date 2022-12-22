#!/usr/bin/python3


def safe_print_intefer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
