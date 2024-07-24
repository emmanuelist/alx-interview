#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, amount):
    """
    This function calculates the minimum number of coins required
    to make a given amount of change.
    It uses a greedy algorithm to find the optimal solution,
    assuming that the coins are available in
    infinite quantities and the denominations are distinct.

    Parameters:
    coins (List[int]): A list of integers representing the
    available coin denominations.
    amount (int): The target amount of change to be made.

    Returns:
    int: The minimum number of coins required to make the given
    amount of change. If it's not possible to make the
    exact amount using the given coins, it returns -1.
    """
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        amount -= num * coin
        count += num
    return count if amount == 0 else -1
