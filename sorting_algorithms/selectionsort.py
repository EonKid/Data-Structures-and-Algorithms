#!/bin/python3

"""
Selection Sort

Sort list by finding index and pushing to left/right

Time complexity
Best case: O(n*n)
Average case: O(n*n)
Worst case: O(n*n)
"""


def find_minimum_index(A: [int], start_index: int) -> int:
    minimum_index = start_index
    for start_index in range(start_index+1, len(A)):
        if A[minimum_index] > A[start_index]:
            minimum_index = start_index
    return minimum_index


def sort(A: [int]) -> [int]:
    """
    List of integer to be sorted
    :param A:
    :type A:
    :return:
    :rtype:
    """
    for i in range(0, len(A)):
        min_index = find_minimum_index(A, start_index=i)
        A[i], A[min_index] = A[min_index], A[i]
    return A



L = [5, 4, 3, 2, 1]
print(sort(L))
