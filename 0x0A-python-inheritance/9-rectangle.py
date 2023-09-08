#!/usr/bin/python3
""" module subclass rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """ Computes the area of instance for the class Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ Returns String repr of instance for the class Rectangle
        """
        return f"[Rectangle] "{self.__width}/{self.__height)"
