#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    transformed_dict = a_dictionary.copy()
    for key in a_dictionary:
        transformed_dict[key] *= 2
    return transformed_dict
