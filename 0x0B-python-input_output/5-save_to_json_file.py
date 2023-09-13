#!/usr/bin/python3

"""Implements Persistence Of Serialized Obj."""
import json


def save_to_json_file(my_obj, filename):
    """Persists a serialized PyObj."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
