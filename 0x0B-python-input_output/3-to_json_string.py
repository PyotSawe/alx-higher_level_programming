#!/usr/bin/python3
"""Implements Object Serialization."""
import json


def to_json_string(my_obj):
    """Return Obj State Represent As JSON"""
    return json.dumps(my_obj)
