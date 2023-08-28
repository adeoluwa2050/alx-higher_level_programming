#!/usr/bin/python3
""" module subclass rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
