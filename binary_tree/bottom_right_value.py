class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

def bottom_right_value(root):
    """
    Write a function, bottom_right_value, that takes in the root of a binary tree.
    The function should return the right-most value in the bottom-most level of the tree.
    You may assume that the input tree is non-empty.
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """

    if not root:
        return
    curr = root
    q = deque([root])
    while q:
        curr = q.popleft()
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return curr.val


if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(10)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     10
    #  / \      \
    # 4   -2     1

    bottom_right_value(a)  # -> 1
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \
    #    -2  6

    bottom_right_value(a)  # -> 6
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)
    i = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \    /
    #    -2  6  7

    bottom_right_value(a)  # -> 7
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.right = d
    d.left = e
    e.right = f

    #      a
    #    /   \
    #   b     c
    #    \
    #     d
    #    /
    #   e
    #   \
    #    f

    bottom_right_value(a)  # -> 'f'
    a = Node(42)

    #      42

    bottom_right_value(a)  # -> 42