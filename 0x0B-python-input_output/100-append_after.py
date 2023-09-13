#!/usr/bin/python3
'''
Provides the append-after functionality
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Expressions of how to insert a line to a file
    '''
    append_text = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            append_text += line
            if search_string in line:
                append_text += new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(append_text)
