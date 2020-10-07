#!/usr/bin/python3

"""
This is a module for load_from_json_file.
"""

import json


def load_from_json_file(filename):
    """Create an Object from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)