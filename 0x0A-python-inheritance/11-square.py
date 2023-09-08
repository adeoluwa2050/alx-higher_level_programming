#!/usr/bin/python3
"""Module defines class Square
subclass of class Rectangle
"""
BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(BaseGeometry):
    """
    A Square class shape, inherits from BaseGeometry
    """
    def __init__(self, size):
        """"
        Initialize function for Square
        Attributes:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion to print with/height
        Returns:
            Return width/height.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        A function that calculates the area of the Square
        """
        return self.__size ** 2
