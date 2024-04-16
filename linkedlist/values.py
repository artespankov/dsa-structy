class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def linked_list_values(head):
#   if head is None:
#     return []

#   return [head.val, *linked_list_values(head.next)]

# def linked_list_values(head):
#   ans = []
#   while head:
#     ans.append(head.val)
#     head = head.next
#   return ans

def linked_list_values_iter(head):
    """
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


def linked_list_values_rec(head):
    """
    Write a function, linked_list_values, that takes in the head of a linked list as an argument.
    The function should return a list containing all values of the nodes in the linked list.
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    values = []
    def dfs(head, values):
        if head is None:
            return
        values.append(head.val)
        dfs(head.next, values)

    dfs(head, values)
    return values


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    linked_list_values_iter(a)  # -> [ 'a', 'b', 'c', 'd' ]
    x = Node("x")
    y = Node("y")

    x.next = y

    # x -> y

    linked_list_values_iter(x)  # -> [ 'x', 'y' ]
    q = Node("q")

    # q

    linked_list_values_iter(q)  # -> [ 'q' ]
    linked_list_values_iter(None)  # -> [ ]
