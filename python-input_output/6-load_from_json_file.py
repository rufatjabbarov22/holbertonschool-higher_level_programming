#!/usr/bin/python3

'''
    quick doc
'''

import json
from io import StringIO


def load_from_json_file(filename):
    '''
        quick doc
    '''

    output = None
    with open(filename) as f:
        output = json.load(f)
    return output
