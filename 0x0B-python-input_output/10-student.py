#!/usr/bin/python3
'''
Write a class Student that defines a student
'''


class Student:
    '''
    Definition of Info_Obj to Express Student
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Expression of how to construct student_info_obj
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Expression of how to coerse to JSON
        '''
        if attrs is None:
            return self.__dict__
        a_dict = {}
        for props in attrs:
            if hasattr(self, props):
                a_dict[props] = getattr(self, props)
        return a_dict
