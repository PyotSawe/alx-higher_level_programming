#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    prnted = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int and prnted != x:
                print('{:d}'.format(my_list[i]), end='')
                prnted += 1
        except TypeError:
            continue

    print()

    return prnted
