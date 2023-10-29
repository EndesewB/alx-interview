#!/usr/bin/python3
"""UTF-8 Validation's module"""


def validUTF8(data):
    """Initialize a variable to keep track of
    the number of valid leading bytes.
    """
    valid_leading_bytes = 0
    for byte in data:
        if byte >= 128 and byte <= 191:
            if valid_leading_bytes <= 0:
                return False
            valid_leading_bytes -= 1
        else:
            if valid_leading_bytes > 0:
                return False
            if byte < 128:
                valid_leading_bytes = 0
            elif byte >= 192 and byte <= 223:
                valid_leading_bytes = 1
            elif byte >= 224 and byte <= 239:
                valid_leading_bytes = 2
            elif byte >= 240 and byte <= 247:
                valid_leading_bytes = 3
            else:
                return False

    return valid_leading_bytes == 0
