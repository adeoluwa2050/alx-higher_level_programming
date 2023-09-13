#!/usr/bin/python3
""" This is a module that works With JSON files """

import json

def load_from_json_file(filename):
    """ To create an object from JSON file """
    with open(filename, 'r') as open_file:
        return json.load(open_file)
