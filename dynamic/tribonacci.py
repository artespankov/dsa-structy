from functools import lru_cache

@lru_cache(maxsize=None)
def tribonacci(n):
    """
    Time: O(n)
    Space: O(n)
    """
    if n == 1 or n == 0:
        return 0
    if n == 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


m = {}
def tribonacci_rec_memoization(n):
    """
    Time: O(3^n)
    Space: O(n)
    """
    if n in m:
        return m[n]
    if n == 1 or n == 0:
        return 0
    if n == 2:
        return 1
    m[n] = tribonacci_rec_memoization(n-1) + tribonacci_rec_memoization(n-2) + tribonacci_rec_memoization(n-3)
    return m[n]


if __name__ == "__main__":
    tribonacci_rec_memoization(0)  # -> 0
    tribonacci_rec_memoization(1)  # -> 0
    tribonacci_rec_memoization(2)  # -> 1
    tribonacci_rec_memoization(5)  # -> 4
    tribonacci_rec_memoization(7)  # -> 13
    tribonacci_rec_memoization(14)  # -> 927
    tribonacci_rec_memoization(20)  # -> 35890
    tribonacci_rec_memoization(37)  # -> 1132436852