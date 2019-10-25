#!/bin/python3

"""
Bubble Sort

Bubble up the greater element to left/right

Time complexity
Best case: O(n)
Average case: O(n*n)
Worst case: O(n*n)
"""


def sort(A: [int]) -> [int]:
    """
    List of integer to be sorted
    :param A:
    :type A:
    :return:
    :rtype:
    """
    for k in range(0, len(A)):
        is_sorted = True
        for i in range(0, len(A) - k - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                is_sorted = False
        if is_sorted:
            break
    return A


L = [2, 7, 4, 1, 5, 3]
print(sort(L))