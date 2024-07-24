#!/usr/bin/python3


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list of int): A list of coin denominations
    total (int): The total amount to make up.

    Returns:
    int: The minimum number of coins needed to make up the total amount,
    or -1 if it is not possible.

    """

    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each amount
    dp = [float("inf")] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Loop through each coin and update the dp list
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # if dp[total] is still infinity, it means
    # it's not possible to make that amount
    return dp[total] if dp[total] != float("inf") else -1
