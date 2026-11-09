def uncompress(s):
    """
    Write a function, uncompress, that takes in a string as an argument.
    The input string will be formatted into multiple groups according to the following pattern:
    <number><char>
    for example, '2c' or '3a'.
    The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively.
    You may assume that the input string is well-formed according to the previously mentioned pattern.

    n = number of groups
    m = max num found in any group
    Time: O(n*m)
    Space: O(n*m)
    """
    result = []
    i, j = 0, 0
    while j < len(s):
        while j < len(s) and s[i] == s[j]:
            j += 1
        if j-i > 1:
            result.append(str(j-i))
        result.append(s[i])
        i = j
    return "".join(result)


    # numbers = '0123456789'
    # result = []
    # i = 0
    # j = 0
    # while j < len(s):
    #     if s[j] in numbers:
    #     j += 1
    #     else:
    #     num = int(s[i:j])
    #     result.append(s[j] * num)
    #     j += 1
    #     i = j

    # return ''.join(result)





if __name__ == "__main__":
    uncompress("2c3a1t") # -> 'ccaaat'
    uncompress("4s2b") # -> 'ssssbb'
    uncompress("2p1o5p") # -> 'ppoppppp'
    uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
    uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
