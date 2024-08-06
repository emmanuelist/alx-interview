#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.

This module contains a single function `canUnlockAll` that checks if all boxes
in a list of lists can be unlocked starting from the first box.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list where each element
        is a list of keys contained in a box.
        The index of the list represents the box number.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Check if the input is valid
    if not boxes or not isinstance(boxes, list):
        return False

    # List to keep track of unlocked boxes, starting with the first box
    unlocked = [0]

    # Iterate through a copy of the list of unlocked boxes
    for n in unlocked:
        # Iterate through the keys in the current box
        for key in boxes[n]:
            # If the key opens a new box and the box number is valid
            if key not in unlocked and key < len(boxes):
                # Add the box to the list of unlocked boxes
                unlocked.append(key)

    # Check if the number of unlocked boxes equals the total number of boxes
    if len(unlocked) == len(boxes):
        return True
    return False
