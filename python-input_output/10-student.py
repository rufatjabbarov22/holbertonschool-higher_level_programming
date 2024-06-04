#!/usr/bin/python3

'''
    quick doc
'''


class Student():
    '''
        quick doc
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        sattrs = {
            key: getattr(self, key)
            for key in dir(self)
            if key[:2] != "__"
            and key != "to_json"
            }
        if attrs is None:
            return sattrs
        else:
            return {
                key: sattrs[key]
                for key in sattrs
                if key in attrs
                }
