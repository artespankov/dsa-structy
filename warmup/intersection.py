def intersection1(a, b):
    """
    O(n*m)
    O(min(n,m))
    """
    result = []
    for item in b:
        if item in a:
            result.append(item)
    return result


def intersection(a, b):
    """
    intersection
    Write a function, intersection, that takes in two lists, a,b, as arguments.
    The function should return a new list containing elements that are in both of the two lists.

    You may assume that each input list does not contain duplicate elements.
    n = array a size, m = array b size
    Time: O(n+m)
    Space: O(m)
    """
    b_set = set(b)
    return [num for num in a if num in b_set]


if __name__ == "__main__":
    intersection([4, 2, 1, 6], [3, 6, 9, 2, 10])  # -> [2,6]
    intersection([2, 4, 6], [4, 2])  # -> [2,4]
    intersection([4, 2, 1], [1, 2, 4, 6])  # -> [1,2,4]
    intersection([0, 1, 2], [10, 11])  # -> []
    a = [i for i in range(0, 50000)]
    b = [i for i in range(0, 50000)]
    intersection(a, b)  # -> [0,1,2,3,..., 49999]
