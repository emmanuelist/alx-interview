#!/usr/bin/python3

"""
utf8validator module

This module provides a function to validate a sequence of bytes as a valid
UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate a sequence of bytes as a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing bytes in the range
        0-255.

    Returns:
        bool: True if the input data is a valid UTF-8 encoding, False
        otherwise.

    Example:
        >>> validUTF8([197, 130, 1])  # valid UTF-8 encoding for "Á"
        True
        >>> validUTF8([250, 130, 1])  # invalid UTF-8 encoding
        False
    """
    num_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if num_bytes == 0:
            if bin_rep[0] == '0':
                continue
            elif bin_rep[:3] == '110':
                num_bytes = 1
            elif bin_rep[:4] == '1110':
                num_bytes = 2
            elif bin_rep[:5] == '11110':
                num_bytes = 3
                return False
        else:
            if bin_rep[:2] != '10':
                return False
            num_bytes -= 1

    return num_bytes == 0
