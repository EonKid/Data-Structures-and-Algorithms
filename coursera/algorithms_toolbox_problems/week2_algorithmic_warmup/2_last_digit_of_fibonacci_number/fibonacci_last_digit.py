# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    result = 0
    previous = 0
    current  = 1

    for _ in range(n - 1):
        result = (previous + current) % 10
        previous, current = current, result


    return result


n = int(input())
print(get_fibonacci_last_digit_naive(n))
