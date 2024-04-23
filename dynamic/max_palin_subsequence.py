def max_palin_subsequence(string):
    """
    Write a function, max_palin_subsequence, that takes in a string as an argument.
    The function should return the length of the longest subsequence of the string that is also a palindrome.
    A subsequence of a string can be created by deleting any characters of the string,
    while maintaining the relative order of characters.
    n = length of the string
    Time: O(n^2)
    Space: O(n)

    with memoization
    Time: O(n^2)
    Space: O(n^2)
    """
    return _max_palin_subsequence(string, 0, len(string) - 1, {})


def _max_palin_subsequence(string, start, end, memo):
    substring = (start, end)

    if substring in memo:
        return memo[substring]

    # 1- character string
    if end == start:
        return 1

    # empty string
    if end < start:
        return 0

    # first and last characters are the same
    if string[start] == string[end]:
        memo[substring] = 2 + _max_palin_subsequence(string, start + 1, end - 1, memo)
    else:
        without_leading = 0 + _max_palin_subsequence(string, start + 1, end, memo)
        without_ending = 0 + _max_palin_subsequence(string, start, end - 1, memo)
        memo[substring] = max(without_leading, without_ending)
    return memo[substring]


if __name__ == "__main__":
    max_palin_subsequence("luwxult")  # -> 5
    max_palin_subsequence("xyzaxxzy")  # -> 6
    max_palin_subsequence("lol")  # -> 3
    max_palin_subsequence("boabcdefop")  # -> 3
    max_palin_subsequence("z")  # -> 1
    max_palin_subsequence("chartreusepugvicefree")  # -> 7
    max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty")  # -> 15
    max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe")  # -> 31