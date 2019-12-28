#!/bin/python3

"""
Insertion sort
Sort list of integers using shifting sorted array size from left to right

Time complexity:
Best case: O(n)
Avergare case: O(n*n)
Worst case: O(n*n)
"""


def sort(A):
    for i in range(1, len(A)):
        value = A[i]
        hole = i
        while hole > 0 and A[hole -1] > value:
            A[hole] = A[hole - 1]
            hole -= 1
        A[hole] = value
    return A


L = [7, 2, 4, 1, 5, 3]
print(sort(L))