def is_palindrome(s):
    """
    Write a function, is_palindrome, that takes in a string and
    returns a boolean indicating whether or not the string is the same forwards and backwards.
    Time: O(n)
    Space: O(1)
    """
    L, R = 0, len(s)-1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True


if __name__ == "__main__":
    is_palindrome("pop") # -> True
    is_palindrome("kayak") # -> True
    is_palindrome("pops") # -> False
    is_palindrome("boot") # -> False
    is_palindrome("rotator") # -> True
    is_palindrome("abcbca") # -> False
    is_palindrome("") # -> True
