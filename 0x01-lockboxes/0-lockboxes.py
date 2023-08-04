#usr/bin/python3

"""
a function to determine if all boxes have been visited 
@Boxes: boxes containing keys
return true if all boxes have been unlocked else false
"""


def canUnlockAll(boxes):
    """
    a function to determine if all boxes have been visited"""

    # check if boxes is a list
    if type(boxes) is not list:
        return False
    # check if boxes is empty
    if len(boxes) == 0:
        return False
    # check if boxes is a list of list
    for box in boxes:
        if type(box) is not list:
            return False
    # check if boxes[0] is empty
    if len(boxes[0]) == 0:
        return False
    # check if boxes[0] contains 0
    if 0 not in boxes[0]:
        return False
    # check if boxes[0] contains a key to another box
    for key in boxes[0]:
        if key < len(boxes):
            if key != 0:
                if 0 in boxes[key]:
                    return False
    # check if all boxes can be opened
    for i in range(1, len(boxes)):
        if i not in boxes[i]:
            return False
    # return true if all boxes can be opened
    return True
