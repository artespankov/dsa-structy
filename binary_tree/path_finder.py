class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def path_finder(root, target):
    """
    Write a function, path_finder, that takes in the root of a binary tree and a target value.
    The function should return an array representing a path to the target value.
    If the target value is not found in the tree, then return None.
    You may assume that the tree contains unique values.

    n = number of nodes
    Time: O(n^2)
    Space: O(n)
    """
    if not root:
        return None
    if root.val == target:
        return [root.val]
    left = path_finder(root.left, target)
    right = path_finder(root.right, target)
    if left:
        return [root.val] + [*left]
    if right:
        return [root.val] + [*right]
    return None


def path_finder_append(root, target):
    """
    with append
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    result = _path_finder(root, target)
    return result[::-1] if result else None


def _path_finder(root, target):
    if root is None:
        return None
    if root.val == target:
        return [root.val]

    left = _path_finder(root.left, target)
    right = _path_finder(root.right, target)

    if left:
        left.append(root.val)
        return left
    if right:
        right.append(root.val)
        return right


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    path_finder(a, 'e')  # -> [ 'a', 'b', 'e' ]
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    path_finder(a, 'p')  # -> None
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    path_finder(a, "c")  # -> ['a', 'c']
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    path_finder(a, "h")  # -> ['a', 'c', 'f', 'h']
    x = Node("x")

    #      x

    path_finder(x, "x")  # -> ['x']
    path_finder(None, "x")  # -> None
    root = Node(0)
    curr = root
    for i in range(1, 19500):
        curr.right = Node(i)
        curr = curr.right

    #      0
    #       \
    #        1
    #         \
    #          2
    #           \
    #            3
    #             .
    #              .
    #               .
    #              19498
    #                \
    #                19499

    path_finder(root, 16281)  # -> [0, 1, 2, 3, ..., 16280, 16281]
