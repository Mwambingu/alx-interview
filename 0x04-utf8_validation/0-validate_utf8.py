#!/usr/bin/python3
"""
Contains a UTF-8 Validation Function
"""


def validUTF8(data):
    """
    UTF-8 Validator function
    """
    count = 0
    for d in data:
        if count == 0:
            if count == 0:
                if d & 128 == 0:
                    count = 0
                elif d & 224 == 192:
                    count = 1
                elif d & 240 == 224:
                    count = 2
                elif d & 248 == 240:
                    count = 3
                else:
                    return False
            else:
                if d & 192 != 128:
                    return False
                count -= 1
    if count == 0:
        return True
    return False
