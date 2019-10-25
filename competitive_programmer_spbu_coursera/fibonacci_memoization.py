#!/bin/python3
import sys

"""
Fibonacci number solution using iterative and memoization method
"""

T = dict()

def fib_iterative_list(n):
    A = [None] * (n+1)
    A[0], A[1] = 0, 1
    for i in range(2, n+1):
        A[i] = A[i-1] + A[i-2]
    return A[n]

def fib_iterative(n):
    previous_num, current_num = 0, 1
    for _ in range(n-1):
        new_current = previous_num + current_num
        previous_num, current_num = current_num, new_current
    return current_num


def fib(n):
    if n not in T:
        if n <= 1:
            T[n] = 1
        else:
            T[n] = fib(n-1) + fib(n-2)
    return T[n]

n = int(input())

print('maxinmum recursion limit: ', sys.getrecursionlimit())
print('Memoization with recursion: ', fib(n))
print('Iterative without using list: ', fib_iterative(n))
print('Iterative with memoization: ', fib_iterative_list(n))
