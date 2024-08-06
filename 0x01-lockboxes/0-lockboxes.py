#!/usr/bin/python3

def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)

    # Set to keep track of opened boxes
    opened = set()

    # Stack for DFS, starting with the first box
    stack = [0]

    # While there are boxes to explore
    while stack:
        # Get the current box
        current_box = stack.pop()

        # If the box is not already opened
        if current_box not in opened:
            # Mark it as opened
            opened.add(current_box)

            # Add all keys from this box to the stack
            for key in boxes[current_box]:
                if key < n and key not in opened:
                    stack.append(key)

    # Check if all boxes are opened
    return len(opened) == n
