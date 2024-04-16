def pair_sum(numbers, target_sum):
    """
    Write a function, pair_sum, that takes in a list and a target sum as arguments.
    The function should return a tuple containing a pair of indices whose elements sum to the given target.
    The indices returned must be unique.
    Be sure to return the indices, not the elements themselves.
    There is guaranteed to be one such pair that sums to the target.
    n = array size
    Time: O(n)
    Space: O(n)
    """
    pairs_sum = {}
    for i, num in enumerate(numbers):
        if (target_sum - num) in pairs_sum:
            return pairs_sum[target_sum - num], i
        pairs_sum[num] = i


if __name__ == "__main__":
    assert pair_sum([3, 2, 5, 4, 1], 8) == (0, 2)
    assert pair_sum([4, 7, 9, 2, 5, 1], 5) == (0, 5)
    assert pair_sum([4, 7, 9, 2, 5, 1], 3) == (3, 5)
    assert pair_sum([1, 6, 7, 2], 13) == (1, 2)
    assert pair_sum([9, 9], 18) == (0, 1)
    assert pair_sum([6, 4, 2, 8], 12) == (1, 3)