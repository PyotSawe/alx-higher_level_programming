#!/usr/bin/python3
'''
Write a function that returns
the dictionary description with
simple data structure of a serialized json
'''


def class_to_json(obj):
    '''
    Returns obj.__dict_ of obj
    '''

    return vars(obj)
