#!/usr/bin/python3

"""Implements Deserialization."""
import json


def from_json_string(my_str):
    """Return Desrialized Python Obj."""
    return json.loads(my_str)
