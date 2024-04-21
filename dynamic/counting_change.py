def counting_change(amount, coins):
    """
    Write a function, counting_change, that takes in an amount and a list of coins.
    The function should return the number of different ways it is possible
    to make change for the given amount using the coins.
    You may reuse a coin as many times as necessary.
    For example,
    counting_change(4, [1,2,3]) -> 4
    There are four different (!!!UNIQUE!!!) ways to make an amount of 4:

    1. 1 + 1 + 1 + 1
    2. 1 + 1 + 2
    3. 1 + 3
    4. 2 + 2
    Note:
        3 + 1 is the same way as 1 + 3
        2 + 1 + 1 is the same as 1 + 1 + 2 & 1 + 2 + 1
        so out of 7 total paths we choose only 4 unique ways as a result

    Note on memoization:
        keys to memo should be the pieces of input that dictate the output change,
        for example - amount that decreases with each call or pair of (amount, index) that are changing

    Note on combinations:
        when combinations aren't unique - you need to iterate n*n, i.e. you use every element type
        on every recursion level
                elem1,                 elem2,                  elem3
        [elem1, elem2,elem3]   [elem1, elem2,elem3]    [elem1, elem2,elem3]

        when you need unique combinations only, you should iterate over type of elements only once,
        changing the quantity of elements of every type, from 0 up to allowed limit
            elem1,                     elem2,                  elem3
        x0   0                          0                       0
        x1   1                          1                       1
        x2   2                          2                       2
        x3   3                          3                       3
    """
    return _counting_change(amount, coins, 0, {})


def _counting_change(amount, coins, i, memo):
    """
    a = amount
    c = # coins
    Time: O(a^c), with memoization O(a*c)
    Space: O(a*c)
    """
    key = (i, amount)

    if key in memo:
        return memo[key]

    if amount == 0:
        return 1

    if i == len(coins):
        return 0

    coin_val = coins[i]
    paths = 0
    # in Python, // rounds down, throwing away the decimal part
    for coin_qty in range(0, (amount // coin_val) + 1):
        coins_value = coin_qty * coin_val
        # with each recursive call, we both decrease the amount
        # by the value of the current coin type and chosen quantity
        # and try with the next type of coin
        paths += _counting_change(amount - coins_value, coins, i + 1, memo)
    memo[key] = paths
    return paths