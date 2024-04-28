"""
Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None





from collections import deque
def how_high_bfs(node):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    if not node:
        return -1
    max_height = 0
    q = deque([(node, max_height)])

    while q:
        curr, height = q.popleft()
        if not curr.left and not curr.right:
            max_height = max(max_height, height)

        if curr.left:
            q.append((curr.left, height + 1))
        if curr.right:
            q.append((curr.right, height + 1))
    return max_height





def how_high_dfs(node):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    if not node:
        return -1
    max_height = 0
    s = [(node, max_height)]

    while s:
        curr, height = s.pop()
        if not curr.left and not curr.right:
            max_height = max(max_height, height)

        if curr.left:
            s.append((curr.left, height + 1))
        if curr.right:
            s.append((curr.right, height + 1))
    return max_height


def how_high(node):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    if not node:
        return -1
    return 1 + max(how_high(node.left), how_high(node.right))


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

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

    how_high(a)  # -> 2
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    how_high(a)  # -> 3
    a = Node('a')
    c = Node('c')

    a.right = c

    #      a
    #       \
    #        c

    how_high(a)  # -> 1
    a = Node('a')

    #      a

    how_high(a)  # -> 0
    how_high(None)  # -> -1