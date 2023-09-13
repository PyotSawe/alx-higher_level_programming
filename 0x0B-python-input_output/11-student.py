#!/usr/bin/python3
'''
Definition of Student Info_Objs
'''


class Student:
    '''
    Student Info_Obj
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Expression of construct the info_obj @rt
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Retrieves dict
        '''
        if attrs is None:
            return self.__dict__
        a_dict = {}
        for props in attrs:
            if hasattr(self, props):
                a_dict[props] = getattr(self, props)
        return a_dict

    def reload_from_json(self, json):
        '''
        Updates the attributes with json attributes
        '''
        self.__dict__.update(json)
