#!/usr/bin/python3
"""
"""


def makeChange(coins, total):
    """
    This function calculates the minimum number of coins required to make a
    given total amount using a given set of coin denominations.
    It uses dynamic programming to efficiently solve this problem.

    Parameters:
    coins (list of int): A list of coin denominations.
    Each element in the list represents a coin denomination.
    total (int): The total amount to be made using the given
    coin denominations.

    Returns:
    int: The minimum number of coins required to make the total amount.
    If it is not possible to make the total amount using the given coin
    denominations, it returns -1.
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
