
def uncompress(s):
    """
    Write a function, uncompress, that takes in a string as an argument.
    The input string will be formatted into multiple groups according to the following pattern:
    <number><char>

    for example, '2c' or '3a'.
    The function should return an uncompressed version of the string where each 'char' of a group
    is repeated 'number' times consecutively.
    You may assume that the input string is well-formed according to the previously mentioned pattern.
    n = number of groups
    m = max num found in any group
    Time: O(n^2*m)
    Space: O(n*m)
    """
    res = ''
    i = 0
    while i < len(s):
        num = ''
        while s[i] in '1234567890' and i < len(s):
            num += s[i]
            i += 1
        res += int(num) * s[i]
        i += 1
    return res

def uncompress2(s):
    """
    n = number of groups
    m = max num found in any group
    Time: O(n*m) - improve with list instead of string used to accumulate result
    Space: O(n*m)
    """
    res = []
    i = 0
    j = 0
    nums = "0123456789"
    while j < len(s):
        if s[j] in nums:
            j += 1
        else:
            num = int(s[i:j])
            res.append(num * s[j])
            j += 1
            i = j
    return "".join(res)


if __name__ == "__main__":
    assert uncompress("2c3a1t") =='ccaaat'
    assert uncompress("4s2b") == 'ssssbb'
    assert uncompress("2p1o5p") == 'ppoppppp'
    assert uncompress("3n12e2z") == 'nnneeeeeeeeeeeezz'
    assert uncompress("127y") == 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

    assert uncompress2("2c3a1t") == 'ccaaat'
    assert uncompress2("4s2b") == 'ssssbb'
    assert uncompress2("2p1o5p") == 'ppoppppp'
    assert uncompress2("3n12e2z") == 'nnneeeeeeeeeeeezz'
    assert uncompress2("127y") == 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
