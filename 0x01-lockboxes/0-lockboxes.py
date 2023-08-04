#!/usr/bin/python3

"""
a function to determine if all boxes have been visited
@boxes: boxes containing keys
return true if all boxes can be unlocked else false
"""


def canUnlockAll(boxes):

    """
    create a set to keep track of all boxes visited
    """
    visited = set()
    visited.add(0)

    stack = [0]

    # perform DFS
    while stack:
        box = stack.pop()

        # check if you have a key to open other boxes
        for key in boxes[box]:
            if key not in visited:
                visited.add(key)
                stack.append(key)

    # check if all boxes have been visited
    return len(visited) == len(boxes)