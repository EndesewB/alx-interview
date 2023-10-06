#!/usr/bin/python3
"""a function  that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
