#!/usr/bin/python3

"""Saves All CMD_ARGS to file"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
if __name__ == "__main__":
    filename = "add_item.json"
    try:
        my_items = load_from_json_file(filename)
    except FileNotFoundError:
        my_items = []
    for i in range(1, len(argv)):
        my_items.append(argv[i])
    save_to_json_file(my_items, filename)
