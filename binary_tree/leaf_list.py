class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leaf_list(root):
    """
    Write a function, leaf_list, that takes in the root of a binary tree
    and returns a list containing the values of all leaf nodes in left-to-right order.
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    res = []
    s = [root]
    while s:
        curr = s.pop()
        if curr.right is None and curr.left is None:
            res.append(curr.val)
        if curr.right:
            s.append(curr.right)
        if curr.left:
            s.append(curr.left)
    return res


def leaf_list_rec(root):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    def dfs(root, leaves):
        if not root:
            return
        if root.left is None and root.right is None:
            leaves.append(root.val)
        dfs(root.left, leaves)
        dfs(root.right, leaves)
    leaves = []
    dfs(root, leaves)
    return leaves


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

    leaf_list(a)  # -> [ 'd', 'e', 'f' ]
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

    leaf_list(a)  # -> [ 'd', 'g', 'h' ]
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \
    # 20   15
    #      / \
    #     1  3

    leaf_list(a)  # -> [ 20, 1, 3, 54 ]
    x = Node('x')

    #      x

    leaf_list(x)  # -> [ 'x' ]
    leaf_list(None)  # -> [ ]