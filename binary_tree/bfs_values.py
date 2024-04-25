from collections import deque


class Node:
    
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def breadth_first_values(root):
    """
    Write a function, breadth_first_values, that takes in the root of a binary tree.
    The function should return a list containing all values of the tree in breadth-first order.
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    ans = []
    if root is None:
        return ans

    queue = deque([root])
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans


# TEST 0
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

breadth_first_values(a)
#    -> ['a', 'b', 'c', 'd', 'e', 'f']


# TEST 1
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

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

# TEST 2
breadth_first_values(a)
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a = Node('a')

#      a

# TEST 3
breadth_first_values(a)
#    -> ['a']
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e

breadth_first_values(a)
#    -> ['a', 'b', 'c', 'x', 'd', 'e']


# TEST 4
breadth_first_values(None)
#    -> []
