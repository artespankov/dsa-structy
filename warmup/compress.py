def compress(s):
    """
    Write a function, compress, that takes in a string as an argument.
    The function should return a compressed version of the string where consecutive occurrences
    of the same characters are compressed into the number of occurrences followed by the character.
    Single character occurrences should not be changed.

    'aaa' compresses to '3a'
    'cc' compresses to '2c'
    't' should remain as 't'
    You can assume that the input only contains alphabetic characters.

    n = length of string
    Time: O(n)
    Space: O(n)
    """

    L, R = 0, 0
    res = []
    while R <= len(s):
        if R == len(s) or s[L] != s[R]:
            mul = f"{R - L}" if R - L > 1 else ""
            res.append(f"{mul}{s[L]}")
            L = R
        R += 1
    return "".join(res)


if __name__ == "__main__":
    compress('ccaaatsss')  # -> '2c3at3s'
    compress('ssssbbz')  # -> '4s2bz'
    compress('ppoppppp')  # -> '2po5p'
    compress('nnneeeeeeeeeeeezz')  # -> '3n12e2z'
    compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy') # -> '127y'