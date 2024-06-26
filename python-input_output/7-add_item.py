#!/usr/bin/python3

'''
    quick doc
'''

from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    for arg in argv[1:]:
        try:
            content = load_from_json_file("add_item.json")
        except Exception:
            content = []
        content.append(arg)
        save_to_json_file(content, "add_item.json")
