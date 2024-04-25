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
    if not root:
        return []
    return [root.val, *depth_first_values(root.left), *depth_first_values(root.right)]


def depth_first_values(root):
    """
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