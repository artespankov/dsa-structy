


import math


def helper(amount, coins, memo):
    """
    Write a function min_change that takes in an amount and a list of coins.
    The function should return the minimum number of coins required to create the amount.
    You may use each coin as many times as necessary.
    If it is not possible to create the amount, then return -1.
    c - number of coins
    a - amount
    Time: O(c^a); with memoization O(c*a)
    Space: O(a)
    """
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return amount
    if amount < 0:
        return math.inf

    min_val = math.inf
    for c in coins:
        min_val = min(min_val, helper(amount - c, coins, memo))
    memo[amount] = min_val + 1
    return memo[amount]


def min_change(amount, coins):
    memo = {}
    ans = helper(amount, coins, memo)
    return ans if ans != math.inf else -1




if __name__ == "__main__":
    min_change(8, [1, 5, 4, 12])  # -> 2, because 4+4 is the minimum coins possible
    min_change(13, [1, 9, 5, 14, 30])  # -> 5
    min_change(23, [2, 5, 7])  # -> 4
    min_change(102, [1, 5, 10, 25])  # -> 6
    min_change(200, [1, 5, 10, 25])  # -> 8
    min_change(2017, [4, 2, 10])  # -> -1
    min_change(271, [10, 8, 265, 24])  # -> -1
    min_change(0, [4, 2, 10])  # -> 0
    min_change(0, [])  # -> 0