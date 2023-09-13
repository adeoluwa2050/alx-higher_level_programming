#!/usr/bin/python3
""" This is My Class module
"""

class MyClass:
    """ My class
    """
    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
