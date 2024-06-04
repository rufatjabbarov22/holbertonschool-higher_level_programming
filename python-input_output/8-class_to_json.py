#!/usr/bin/python3

'''
    quick doc
'''


def class_to_json(obj):
    '''
        quick doc
    '''

    return {key: getattr(obj, key) for key in dir(obj) if key[:2] != "__"}
