def is_subsequence(string_1, string_2):
    """
    Write a function, is_subsequence, that takes in string_1 and string_2.
    The function should return a boolean indicating whether or not string_1 is a subsequence of string_2.
    A subsequence is a string that can be formed by deleting 0 or more characters from another string.
    n = length of string_1, m = length of string_2
    Time: O(m)
    Space: O(1)
    """
    i1, i2 = 0, 0
    while i1 < len(string_1) and i2 < len(string_2):
        if string_1[i1] == string_2[i2]:
            i1 += 1
        i2 += 1
    return i1 == len(string_1)

if __name__ == "__main__":
    is_subsequence("bde", "abcdef") # -> True
    is_subsequence("bda", "abcdef") # -> False
    is_subsequence("ser", "super") # -> True
    is_subsequence("serr", "super") # -> False
    is_subsequence("ama", "camera") # -> True
    is_subsequence("unfun", "unfortunate") # -> True
    is_subsequence("riverbed", "river") # -> False
    is_subsequence("river", "riverbed") # -> True
