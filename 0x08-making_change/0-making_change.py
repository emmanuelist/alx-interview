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

    # Initialize dp array with total + 1 (impossible value)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try every coin
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # if dp[total] is still infinity, it means
    # it's not possible to make that amount
    return dp[total] if dp[total] != float('inf') else -1
