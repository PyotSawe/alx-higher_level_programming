#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0

    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print('Inside res: {}'.format(res))
        return res
