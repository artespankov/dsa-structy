import math


def is_prime(n):
    """
    Time: O(n) - iterative approach for i in the range 2,n-1
    Time: O(sqrt(n)) - math trick when unique factors are before the sqrt(n)
    and after that - only the duplicate pairs of factors
    Space: O(1) for both approaches
    """
    if n < 2:
        return False

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(25) is False
    assert is_prime(31) is True
    assert is_prime(2017) is True
    assert is_prime(2048) is False
    assert is_prime(1) is False
    assert is_prime(713) is False
