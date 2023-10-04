#!/usr/bin/python3
"""
Unlock boxes
"""


def can_unlock_all(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of boxes, where each box is represented as a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        box = stack.pop()
        visited[box] = True

        for key in boxes[box]:
            if key < n and not visited[key]:
                stack.append(key)

    return all(visited)
