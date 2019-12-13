# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    result = 0

    for _ in range(n - 1):
        result = (previous + current) % m
        previous, current = current, result

    return result


n, m = map(int, input().split())
print(get_fibonacci_huge_naive(n, m))
