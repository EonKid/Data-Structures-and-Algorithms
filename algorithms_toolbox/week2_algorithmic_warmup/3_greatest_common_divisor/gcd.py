# Uses python3
import sys


def gcd_naive(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


a, b = map(int, input().split())
print(gcd_naive(a, b))
