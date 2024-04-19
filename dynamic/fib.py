from functools import lru_cache
def fib(n):
    """
    Time: O(n)
    Space: O(1)
    """
    n1 = 0
    n2 = 1
    if n == 0:
        return n1
    if n == 1:
        return n2
    i = 2
    while i != n:
        n1, n2 = n2, n1 + n2
        i += 1
    return n1 + n2


def fib_rec1(n):
    """
    Time: O(2^n)
    Space: O(n)
    """
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

@lru_cache(maxsize=None)
def fib_rec_memoization2(n):
    """
    Time: O(n) 2*n ~ n
    Space: O(n)
    """
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib_rec2(n):
    return _fib(n, {})

def _fib(n, memo):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = _fib(n-1, memo) + _fib(n-2, memo)
    return memo[n]


if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(35) == 9227465
    assert fib(46) == 1836311903
    # assert fib(120) == 1836311903

    assert fib_rec2(0) == 0
    assert fib_rec2(1) == 1
    assert fib_rec2(2) == 1
    assert fib_rec2(3) == 2
    assert fib_rec2(4) == 3
    assert fib_rec2(5) == 5
    assert fib_rec2(35) == 9227465
    assert fib_rec2(46) == 1836311903
    assert fib_rec2(120) == 1836311903
