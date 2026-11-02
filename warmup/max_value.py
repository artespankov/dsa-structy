def max_value(nums: list[int]) -> int:
    """
    The function should return the maximum value from the list of numbers.
    """
    return max(nums)


if __name__ == "__main__":

    for result in [
        max_value([2, 5, 1, 1, 4]),  # -> 5
        max_value([1000, 8, 9000]),  # -> 9000
        max_value([1000, 8]),  # -> 1000
        max_value([42]),  # -> 42
        max_value([-5, -2, -1, -11]),  # -> -1
        max_value([-5, -2, -1, -11]),  # -> -1
        max_value([-5, -2, -1, -11]),  # -> -1
    ]:
        print(result)
