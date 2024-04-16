class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def is_univalue_list(head):
    """
    The function should return a boolean indicating whether or not the linked list contains exactly one unique value.
    You may assume that the input list is non-empty.
    n = number of nodes
    Time: O(n)
    Space: O(1)
    """
    curr = head
    while curr:
        if curr.val != head.val:
            return False
        curr = curr.next
    return True



def is_univalue_list_rec(head):
    """
    The function should return a boolean indicating whether or not the linked list contains exactly one unique value.
    You may assume that the input list is non-empty.
    n = number of nodes
    Time: O(n)
    Space: O(n)
    """
    # if not head:
    #     return True
    #
    # if prev_val and head.val != prev_val:
    #     return False
    #
    # return is_univalue_list(head.next, head.val)

    if not head or not head.next:
        return True
    return head.val == head.next.val and is_univalue_list(head.next)




if __name__ == "__main__":
    a = Node(7)
    b = Node(7)
    c = Node(7)

    a.next = b
    b.next = c

    # 7 -> 7 -> 7

    is_univalue_list(a)  # True
    a = Node(7)
    b = Node(7)
    c = Node(4)

    a.next = b
    b.next = c

    # 7 -> 7 -> 4

    is_univalue_list(a)  # False
    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 2 -> 2 -> 2 -> 2

    is_univalue_list(u)  # True
    u = Node(2)
    v = Node(2)
    w = Node(3)
    x = Node(3)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 2 -> 3 -> 3 -> 2

    is_univalue_list(u)  # False
    z = Node('z')

    # z

    is_univalue_list(z)  # True
    u = Node(2)
    v = Node(1)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 1 -> 2 -> 2 -> 2

    is_univalue_list(u)  # False