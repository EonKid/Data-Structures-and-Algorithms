# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    result = 0

    for _ in range(n - 1):
        result = (previous + current) % 10
        previous, current = current,  result
        sum += current
        result = sum % 10

    return result


n = int(input())
print(fibonacci_sum_naive(n))
