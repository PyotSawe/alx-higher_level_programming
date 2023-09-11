#!/usr/bin/python3

"""Defines a BaseGeometry class that raises an exception"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
