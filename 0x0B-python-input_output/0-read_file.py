#!/usr/bin/python3
"""
Module to read and print file contents
"""


def read_file(filename="")
    """To read file and print contents
    """
    with open(filename) as open_file:
        content = open_file.read()
    print(contents, end="")