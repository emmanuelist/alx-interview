#!/usr/bin/python3


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total total.

    Parameters:
    coins (list of int): A list of coin denominations
    total (int): The total total to make up.

    Returns:
    int: The minimum number of coins needed to make up the total total,
    or -1 if it is not possible.

    """

    if total < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        num = total // coin
        total -= num * coin
        count += num
    return count if total == 0 else -1
