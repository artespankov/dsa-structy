class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_min_value_bfs(root):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    ans = root.val
    stack = [root]
    while stack:
        node = stack.pop()
        ans = min(ans, node.val)
        if node.left:
          stack.append(node.left)
        if node.right:
          stack.append(node.right)
    return ans


import math
def tree_min_value_bfs_rec(root):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    if root is None:
        return math.inf
    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))



from collections import deque

def tree_min_value(root):
    """
    BFS
    O(n)
    O(n)
    """
    ans = root.val
    queue = deque([root])
    while queue:
        node = queue.popleft()
        ans = min(ans, node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans


if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
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
    #   11     4
    #  / \      \
    # 4   -2     1
    tree_min_value(a)  # -> -2
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       5
    #    /    \
    #   11     3
    #  / \      \
    # 4   14     12

    tree_min_value(a)  # -> 3
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     /       \
    #    -2       -2

    tree_min_value(a)  # -> -13
    a = Node(42) #        42
    tree_min_value(a)  # -> 42