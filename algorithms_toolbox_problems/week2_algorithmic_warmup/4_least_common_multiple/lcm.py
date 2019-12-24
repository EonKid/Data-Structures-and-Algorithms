# Uses python3
import sys
# a * b = gcd * lcm


def gcd_naive(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def lcm_naive(a, b):
    return min(a*b, (a*b)//gcd_naive(a, b))


a, b = map(int, input().split())
print(lcm_naive(a, b))

