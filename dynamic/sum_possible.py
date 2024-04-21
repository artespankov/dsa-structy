
from functools import lru_cache

def helper(amount, numbers, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return True
    if amount < 0:
        return False
    for num in numbers:
        if helper(amount-num, numbers, memo):
            memo[amount] = True
            return True
        memo[amount] = False
    return False

def sum_possible(amount, numbers):
    """
    Write a function sum_possible that takes in an amount and a list of positive numbers.
    The function should return a boolean indicating whether or not it is possible to create the amount
    by summing numbers of the list.
    You may reuse numbers of the list as many times as necessary.
    You may assume that the target amount is non-negative.
    a = amount
    n = length of numbers
    Time: O(a*n) and O(n^2) without memoization
    Space: O(a)
    """
    return helper(amount, numbers, {})