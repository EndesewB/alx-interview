#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box (box 0)

    while stack:
        box = stack.pop()
        visited[box] = True

        for key in boxes[box]:
            if key < n and not visited[key]:
                stack.append(key)

    return all(visited)
