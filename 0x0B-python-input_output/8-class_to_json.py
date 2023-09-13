#!/usr/bin/python3
""" This is a module for JSON serialization """


def class_to_json(obj):
    """ This returns dictionary description with data list """
    return obj.__dict__
