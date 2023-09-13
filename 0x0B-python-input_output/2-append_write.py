#!/usr/bin/python3
""" This is a Module to append the text to file """


def append_write(filename="", text=""):
    """ Appends the text to file """
    with open(filename, 'a') as open_file:
        count = open_file.write(text)
    return count
