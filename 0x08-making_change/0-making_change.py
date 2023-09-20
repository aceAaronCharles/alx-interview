#!/usr/bin/python3
"""
Task: Change comes from within
Given a pile of coins of different values,
determine the fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    if not coins or total <= 0:
        return -1  # Handle invalid inputs

    coins.sort(reverse=True)  # Sort coins in descending order
    change = 0

    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1

        if total == 0:
            return change  # Successfully made change

    return -1  # Cannot make change for the given total amount
