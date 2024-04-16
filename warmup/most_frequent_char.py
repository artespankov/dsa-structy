from collections import Counter

from collections import Counter


def most_frequent_char(s):
    """
    n - length of the string
    26 - means lowercase eng chars only, so more if upper or other symbols are used
    Time: O(n + 26)
    Space: O(26)
    """
    counters = {}
    for c in s:
        counters[c] = counters.get(c, 0) + 1

    top_freq = 0
    ans = None
    for c in counters:
        if counters[c] > top_freq:
            top_freq = counters[c]
            ans = c
    return ans

def most_frequent_char2(s):

    """
    Write a function, most_frequent_char, that takes in a string as an argument.
    The function should return the most frequent character of the string.
    If there are ties, return the character that appears earlier in the string.
    You can assume that the input string is non-empty.

    n - length of the string
    26 - means lowercase eng chars only, so more if upper or other symbols are used
    Time: O(n + 26)
    Space: O(26)
    """
    counters = Counter(s)
    top_freq = 0
    ans = None
    for c in counters:
        if counters[c] > top_freq:
            top_freq = counters[c]
            ans = c
    return ans


if __name__ == "__main__":
    most_frequent_char('bookeeper')  # -> 'e'
    most_frequent_char('david')  # -> 'd'
    most_frequent_char('abby')  # -> 'b'
    most_frequent_char('mississippi')  # -> 'i'
    most_frequent_char('potato')  # -> 'o'
    most_frequent_char('eleventennine')  # -> 'e'
    most_frequent_char('riverbed')  # -> 'r'
