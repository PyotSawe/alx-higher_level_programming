#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except ZeroDivisionError:
        res = None
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        res = None
        sys.stderr.write("Exception: list index out of range\n")

    return res
