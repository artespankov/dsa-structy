def anagrams(s1, s2):
    """
    Write a function, anagrams, that takes in two strings as arguments.
    The function should return a boolean indicating whether or not the strings are anagrams.
    Anagrams are strings that contain the same characters, but in any order.
    m - length of s1
    n - length of s2
    Time: O(m + n)
    Space: O(m + n)
    """
    freq1 = {}
    for c in s1:
        freq1[c] = freq1.get(c, 0) + 1

    freq2 = {}
    for c in s2:
        freq2[c] = freq2.get(c, 0) + 1

    return freq1 == freq2


from collections import Counter
def anagrams2(s1, s2):
  """
  m - length of s1
  n - length of s2
  Time: O(m + n)
  Space: O(m + n)
  """
  return Counter(s1) == Counter(s2)


if __name__ == "__main__":
    anagrams('restful', 'fluster')  # -> True
    anagrams('cats', 'tocs')  # -> False
    anagrams('monkeyswrite', 'newyorktimes')  # -> True
    anagrams('paper', 'reapa')  # -> False
    anagrams('elbow', 'below')  # -> True
    anagrams('tax', 'taxi')  # -> False
    anagrams('taxi', 'tax')  # -> False
    anagrams('night', 'thing')  # -> True
    anagrams('abbc', 'aabc')  # -> False
    anagrams('po', 'popp')  # -> false
    anagrams('pp', 'oo')  # -> false

    anagrams2('restful', 'fluster')  # -> True
    anagrams2('pp', 'oo')  # -> false
