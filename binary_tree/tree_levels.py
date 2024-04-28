
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


from collections import deque


# def tree_levels(root):
#     if not root:
#         return []
#     q = deque([root])
#     res = [[root.val]]
#     while True:
#         children = deque([])
#         while q:
#             curr = q.popleft()
#             if curr.left:
#                 children.append(curr.left)
#             if curr.right:
#                 children.append(curr.right)
#         if children:
#             res.append([c.val for c in children])
#
#         q = children
#         if not q:
#             break
#     return res


def tree_levels_dfs(root):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    levels = []
    s = [(root, 0)]
    while s:
        curr, lvl = s.pop()
        if len(levels) == lvl:
            levels.append([curr.val])
        else:
            levels[lvl].append(curr.val)
        if curr.right:
            s.append((curr.right, lvl+1))
        if curr.left:
            s.append((curr.left, lvl+1))
    return levels


def tree_levels_bfs(root):
    if not root:
        return []
    levels = []
    q = deque([(root, 0)])
    while q:
        curr, lvl = q.popleft()
        if len(levels) == lvl:
            levels.append([curr.val])
        else:
            levels[lvl].append(curr.val)

        if curr.left:
            q.append((curr.left, lvl+1))
        if curr.right:
            q.append((curr.right, lvl+1))

    return levels

from collections import deque
def tree_levels(root):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    def dfs(root, lvl, levels):
        if not root:
            return
        if len(levels) == lvl:
            levels.append([root.val])
        else:
            levels[lvl].append(root.val)
        dfs(root.left, lvl + 1, levels)
        dfs(root.right, lvl + 1, levels)

    levels = []
    dfs(root, 0, levels)
    return levels



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

    tree_levels(a)  # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f']
    # ]
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #         a
    #      /    \
    #     b      c
    #   /  \      \
    #  d    e      f
    #      / \    /
    #     g  h   i

    tree_levels(a)  # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f'],
    #   ['g', 'h', 'i']
    # ]
    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')
    u = Node('u')
    v = Node('v')

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v

    #      q
    #    /   \
    #   r     s
    #    \
    #     t
    #    /
    #   u
    #  /
    # v

    tree_levels(q)  # ->
    # [
    #   ['q'],
    #   ['r', 's'],
    #   ['t'],
    #   ['u'],
    #   ['v']
    # ]
    tree_levels(None)  # -> []