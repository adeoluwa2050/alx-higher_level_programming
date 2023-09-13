#!/usr/bin/python3
"""
This is the Module for class Student.
"""


class Student:
    """ The Student Class Model """

    def __init__(self, first_name, last_name, age):
        """ Initialize Class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary to JSON """
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            ret = {}
            for p, r in self.__dict__.items():
                if p in attrs:
                    ret[p] = r
            return ret
        else:
            return self.__dict__
