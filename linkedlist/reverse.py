class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list(head):
  """
  Write a function, reverse_list, that takes in the head of a linked list as an argument.
  The function should reverse the order of the nodes in the linked list in-place
   and return the new head of the reversed linked list.
  Time: O(n)
  Space: O(1)
  """
  prev = None
  curr = head
  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  return prev

def reverse_list_rec(head, prev=None):
    """
    Time: O(n)
    Space: O(n)
    """
    if head is None:
        return prev

    nxt = head.next
    head.next = prev

    return reverse_list_rec(nxt, head)


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f

    reverse_list(a) # f -> e -> d -> c -> b -> a

    p = Node("p")

    # p

    reverse_list(p) # p

    x = Node("x")
    y = Node("y")

    x.next = y

    # x -> y

    reverse_list(x) # y -> x