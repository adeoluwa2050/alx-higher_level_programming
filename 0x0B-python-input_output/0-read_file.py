#!/usr/bin/python3
""" This is a module to read and print file contents """

def read_file(filename=""):
    """ To read file and print contents """
    with open(filename) as open_file:
        contents = open_file.read()
    print(contents, end="")
