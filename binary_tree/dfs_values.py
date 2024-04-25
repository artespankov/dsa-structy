from typing import Any


class Node:

    def __init__(self, value: Any, right: 'Node' = None, left: 'Node' = None):
        self.val = value
        self.right = right
        self.left = left


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


#           a
#          / \
#         b   c
#        / \   \
#       d   e   f

def depth_first_values_rec(root):
    """
    n = number of nodes
    Time: O(n^2)
    Space: O(n)
    """
    if not root:
        return []
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val, *left_values, *right_values]


def depth_first_values(root):
    """
    Write a function, depth_first_values, that takes in the root of a binary tree.
    The function should return a list containing all values of the tree in depth-first order.

    Time: O(n)
    Space: O(n) (stack)

    """
    res = []
    if not root:
        return res

    stack = [root]
    while stack:
        # take current from the top of stack
        node = stack.pop()
        if node.val:
            res.append(node.val)
        # left has priority, for stack ~ it was added the last (latter)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res




# =====================
# TESTS
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

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']



# =========
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

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']


# TEST 3
a = Node('a')
#     a
depth_first_values(a)
#   -> ['a']


# TEST 4
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b
b.left = c
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

depth_first_values(a)
#   -> ['a', 'b', 'c', 'd', 'e']


# TEST 5
depth_first_values(None)
#   -> []