class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.next = b
b.next = c
c.next = d


# A -> B -> C -> D -> None

def print_list(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


def print_list_rec(head):
    if head is None:
        return
    print(head.val)
    print_list_rec(head.next)


print_list(a)
print("----")
print_list_rec(a)


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
    """
  O(n)
  O(1)
  """
    sum = 0
    while head is not None:
        sum += head.val
        head = head.next
    return sum


def sum_list_rec(head):
    """
  O(n)
  O(n)
  """
    if head is None:
        return 0
    return head.val + sum_list_rec(head.next)


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

sum_list(a) # 19
