m = {}
def tribonacci(n):
    if n == 1 or n == 0:
        return 0
    if n == 2:
        return 1
    v1 = m[n-1] if n-1 in m else tribonacci(n-1)
    m[n-1] = v1
    v2 = m[n-2] if n-2 in m else tribonacci(n-2)
    m[n-2] = v2
    v3 = m[n-3] if n-3 in m else tribonacci(n-3)
    m[n-3] = v3
    return v1 + v2 + v3


from functools import lru_cache
@lru_cache(maxsize=None)
def tribonacci2(n):
    if n == 1 or n == 0:
        return 0
    if n == 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


if __name__ == "__main__":
    tribonacci(0)  # -> 0
    tribonacci(1)  # -> 0
    tribonacci(2)  # -> 1
    tribonacci(5)  # -> 4
    tribonacci(7)  # -> 13
    tribonacci(14)  # -> 927
    tribonacci(20)  # -> 35890
    tribonacci(37)  # -> 1132436852