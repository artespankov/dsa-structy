def all_unique(items):
    """
    The function should return a boolean indicating whether
    or not the list contains unique items."""

    # T: O(n), S: O(n)
    return len(items) == len(set(items))


if __name__ == "__main__":
    all_unique(["q", "r", "s", "a"])  # -> True
    all_unique(["q", "r", "s", "a", "r", "z"])  # -> False
    all_unique(["red", "blue", "yellow", "green", "orange"])  # -> True
    all_unique(["cat", "cat", "dog"])  # -> False
    all_unique(["a", "u", "t", "u", "m", "n"])  # -> False
