def intersection_with_dupes(a, b):
    """
    intersection with dupes
    Write a function, intersection_with_dupes, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are common to both input lists. The elements in the result should appear as many times as they occur in both input lists.

    You can return the result in any order.
    Time: O(n+m)
    Space: O(m)
    """
    a_count = {}
    b_count = {}

    for num in a:
        a_count[num] = a_count.get(num, 0) + 1

    for num in b:
        b_count[num] = b_count.get(num, 0) + 1

    result = []

    for k, v in a_count.items():
        if k in b_count:
            inter_count = min(v, b_count.get(k, 0))
            result += [k] * inter_count

    return result


from collections import Counter


def intersection_with_dupes_counters(a, b):
    """
    intersection with dupes
    Write a function, intersection_with_dupes, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are common to both input lists. The elements in the result should appear as many times as they occur in both input lists.

    You can return the result in any order.
    Time: O(n+m)
    Space: O(m)
    """
    ac = Counter(a)
    bc = Counter(b)

    res = []
    for k, v in ac.items():
        for i in range(min(v, bc.get(k, 0))):
            res.append(k)

    return res


if __name__ == "__main__":
    print(
        intersection_with_dupes(["a", "b", "c", "b"], ["x", "y", "b", "b"])
    )  # -> ["b", "b"])

    print(
        intersection_with_dupes(["q", "b", "m", "s", "s", "s"], ["s", "m", "s"])
    )  # -> ["m", "s", "s"]

    print(intersection_with_dupes(["p", "r", "r", "r"], ["r"]))  # -> ["r"]

    print(intersection_with_dupes(["t", "v", "u"], ["g", "e", "d", "f"]))  # -> [ ]

    print(
        intersection_with_dupes(
            [
                "a",
                "a",
                "a",
                "a",
                "a",
                "a",
            ],
            ["a", "a", "a", "a"],
        )
    )  # -> ["a", "a", "a", "a"]

    a = []
    b = []
    for i in range(0, 150000):
        a.append(i)
        b.append(i)
    print(intersection_with_dupes(a, b))  # -> [0, 1, 2, ..., 149999]
