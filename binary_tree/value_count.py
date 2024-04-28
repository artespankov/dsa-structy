class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def tree_value_count_rec(root, target):
    """
    Write a function, tree_value_count, that takes in the root of a binary tree and a target value.
    The function should return the number of times that the target occurs in the tree.
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return 0
    root_val = 1 if root.val == target else 0
    return root_val + tree_value_count_rec(root.left, target) + tree_value_count_rec(root.right, target)

def tree_value_count_bfs(root, target):
    """
    n - tree nodes number
    Time: O(n)
    Space: O(n)
    """
    count = 0
    if not root:
        return count
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == target:
            count += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return count


from collections import deque


def tree_value_count_dfs(root, target):
    """
    n - tree nodes number
    Time: O(n)
    Space: O(n)
    """
    count = 0
    if not root:
        return count

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == target:
            count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count

if __name__ == "__main__":
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4   6     12

    tree_value_count(a, 6)  # -> 3
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4  6     12

    tree_value_count(a, 12)  # -> 2
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      7
    #    /   \
    #   5     1
    #  / \     \
    # 1   8     7
    #    /       \
    #   1         1

    tree_value_count(a, 1)  # -> 4
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      7
    #    /   \
    #   5     1
    #  / \     \
    # 1   8     7
    #    /       \
    #   1         1

    tree_value_count(a, 9)  # -> 0
    tree_value_count(None, 42)  # -> 0