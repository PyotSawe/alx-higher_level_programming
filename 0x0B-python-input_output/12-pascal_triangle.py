#!/usr/bin/python3

'''
Provides Pascal interview quiz
'''


def pascal_triangle(n):
    '''
    Expression of how to built a pascal_triangle
    That returns list of lists of integers
    Representing the pascal's triangle of n
    '''
    solution = []
    for level in range(1, n + 1):
        solution.append([1] * level)
    for y in range(2, n):
        row = solution[y]
        prev_row = solution[y - 1]
        for x in range(1, len(row) - 1):
            row[x] = prev_row[x - 1] + prev_row[x]
    return solution
