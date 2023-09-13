#!/usr/bin/python3

"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    with open(filename) as f:
        x = f.read()
        x = f.tell()
        return x
