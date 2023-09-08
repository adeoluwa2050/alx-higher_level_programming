#!/usr/bin/python3
"""Module defines a Rectangle subclass Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize the size of the new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of a square."""

        return self.__size ** 2
        """Returns: int: the area of the square."""
