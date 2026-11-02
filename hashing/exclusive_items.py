def exclusive_items(a, b):
    """
    Write a function, exclusive_items, that takes in two lists, a,b, as arguments.
    The function should return a new list containing elements that are in either list but not both lists.
    You may assume that each input list does not contain duplicate elements.
    """
    # T: O(n+m), S: O(n+m)
    result = []
    sa = set(a)
    sb = set(b)

    for num in sa:
        if num not in sb:
            result.append(num)

    for num in sb:
        if num not in sa:
            result.append(num)

    return result

    # return list(set(a).symmetric_difference(set(b)))


if __name__ == "__main__":

    exclusive_items([4,2,1,6], [3,6,9,2,10]) # -> [4,1,3,9,10]


    exclusive_items([2,4,6], [4,2]) # -> [6]


    exclusive_items([4,2,1], [1,2,4,6]) # -> [6]

    exclusive_items([0,1,2], [10,11]) # -> [0,1,2,10,11]


    a = [ i for i in range(0, 50000) ]
    b = [ i for i in range(0, 50000) ]
    exclusive_items(a, b) # -> [ ]
