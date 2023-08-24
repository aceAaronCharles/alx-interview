#!/usr/bin/python3
"""
UTF-8 Validation module
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes_to_follow = 0

    for num in data:
        # If there are bytes to follow, num must start with 10xxxxxx
        if num_bytes_to_follow:
            if num >> 6 != 0b10:
                return False
            num_bytes_to_follow -= 1
        else:
            # Determine the number of bytes to follow
            if num >> 7 == 0b0:
                num_bytes_to_follow = 0
            elif num >> 5 == 0b110:
                num_bytes_to_follow = 1
            elif num >> 4 == 0b1110:
                num_bytes_to_follow = 2
            elif num >> 3 == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False
    
    return num_bytes_to_follow == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
