#!/usr/bin/python3
"""Module defines class Square
subclass of class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class
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
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

    def area(self):
        """
        A function that calculates the area of the Square
        """
        return self.__size ** 2
