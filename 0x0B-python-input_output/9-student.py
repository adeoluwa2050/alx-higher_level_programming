#!/usr/bin/python3
""" This is a module for Class Student """

class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Initialize class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ To return Dictionary to JSON """
        return self.__dict__
