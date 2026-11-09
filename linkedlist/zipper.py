class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node | None = None


def zipper_lists(head_1, head_2):
    """
    Merge lists 1 & 2
    Alternating each list's elements, in place
    """
    if head_1 and not head_2:
        return head_1
    if head_2 and not head_1:
        return head_2
    first, second = head_1, head_2
    while first and second:
        nxt = first.next
        first.next = second
        first = first.next
        second = nxt
    return head_1


def zipper_lists_2(head_1, head_2):
    """
    n = length of list 1
    m = length of list 2
    Time: O(min(n, m))
    Space: O(1)
    """
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0
    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1
    tail.next = current_1 or current_2
    return head_1


def zipper_lists_rec(head_1, head_2):
    """
    n = length of list 1
    m = length of list 2
    Time: O(min(n, m))
    Space: O(min(n, m))
    """
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1

    head_1_next = head_1.next
    head_1.next = head_2
    head_2.next = zipper_lists(head_1_next, head_2.next)

    return head_1


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    zipper_lists(a, x)
    # a -> x -> b -> y -> c -> z
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

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    zipper_lists(a, x)
    # a -> x -> b -> y -> c -> z -> d -> e -> f

    w = Node("w")
    # w

    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3

    zipper_lists(w, one)
    # w -> 1 -> 2 -> 3

    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3

    w = Node("w")
    # w

    zipper_lists(one, w)
    # 1 -> w -> 2 -> 3
