class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_includes_dfs_rec(root, target):
    """
    Write a function, tree_includes, that takes in the root of a binary tree and a target value.
    The function should return a boolean indicating whether or not the value is contained in the tree.
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    # DFS recursive
    # O(n)
    # O(n)
    if not root or not target:
        return False
    return root.val == target or tree_includes_dfs_rec(root.left, target) or tree_includes_dfs_rec(root.right, target)


def tree_includes_dfs(root, target):
    # DFS
    # O(n)
    # O(n)
    if not root or not target:
        return False
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == target:
          return True
        if node.left:
          stack.append(node.left)
        if node.right:
          stack.append(node.right)
    return False



from collections import deque
def tree_includes_bfs(root, target):
    # BFS
    # O(n)
    # O(n)

  if not root or not target:
    return False
  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node.val == target:
      return True
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return False


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

    tree_includes_bfs(a, "e")  # -> True
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
    tree_includes_bfs(a, "a")  # -> True
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

    tree_includes_bfs(a, "n")  # -> False
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

    tree_includes_bfs(a, "f")  # -> True
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

    tree_includes_bfs(a, "p")  # -> False
    tree_includes_bfs(None, "b")  # -> False