class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_sum_dfs_rec(root):
  # depth first recursive
  # O(n)
  # O(n)
  if not root:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)


def tree_sum_dfs(root):
  # depth first
  # O(n)
  # O(n)
  if not root:
    return 0
  ans = 0
  stack = [root]
  while stack:
    node = stack.pop()
    ans += node.val
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
  return ans


from collections import deque
def tree_sum(root):
    """
    Write a function, tree_sum, that takes in the root of a binary tree that contains number values.
    The function should return the total sum of all values in the tree.
    breadth first
    O(n)
    O(n)
    """
    if not root:
        return 0
    ans = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        ans += node.val
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

    tree_sum(a)  # -> 21
    a = Node(1)
    b = Node(6)
    c = Node(0)
    d = Node(3)
    e = Node(-6)
    f = Node(2)
    g = Node(2)
    h = Node(2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      1
    #    /   \
    #   6     0
    #  / \     \
    # 3   -6    2
    #    /       \
    #   2         2

    tree_sum(a)  # -> 10
    tree_sum(None)  # -> 0