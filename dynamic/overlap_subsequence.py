def overlap_subsequence(string_1, string_2):
    return _overlap_subsequence(string_1, string_2, 0, 0, {})


def _overlap_subsequence(string_1, string_2, pos_1, pos_2, memo):
    """
    Write a function, overlap_subsequence, that takes in two strings as arguments. The function should return the length of the longest overlapping subsequence.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.


    n = length of str1
    m = length of str2
    Time: O(nm)
    Space: O(nm)
    """
    positions = (pos_1, pos_2)
    if positions in memo:
        return memo[positions]
    # one of the strings is empty
    if pos_1 >= len(string_1) or pos_2 >= len(string_2):
        return 0

    subsequence_length = 0
    while pos_1 < len(string_1) and pos_2 < len(string_2) and string_1[pos_1] == string_2[pos_2]:
        subsequence_length += 1
        pos_1 += 1
        pos_2 += 1
    # when there are no more same letters - branch rec for 2 cases - try both strings skipping one next letter
    subsequence_length += max(
        _overlap_subsequence(string_1, string_2, pos_1 + 1, pos_2, memo),
        _overlap_subsequence(string_1, string_2, pos_1, pos_2 + 1, memo)
    )
    memo[positions] = subsequence_length
    return subsequence_length



if __name__ == "__main__":
    overlap_subsequence("dogs", "daogt")  # -> 3
    overlap_subsequence("xcyats", "criaotsi")  # -> 4
    overlap_subsequence("xfeqortsver", "feeeuavoeqr")  # -> 5
    overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave")  # -> 11
    overlap_subsequence(
        "mumblecorebeardleggingsauthenticunicorn",
        "succulentspughumblemeditationlocavore"
    )  # -> 15