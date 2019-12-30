#!/bin/python3

"""
Mergesort

Sort using creating new subarray and merge sorted array back to original array

Time complexity:
Best case: n * log(n)
Average case: n * log(n)
Worst case: n * log(n)

Space complexity: O(n)

"""


def merge(L, R, A):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def sort(A):
    size = len(A)
    if size < 2:
        return
    mid = int(size / 2)
    L = [None] * mid
    R = [None] * (size - mid)
    for i in range(0, mid):
        L[i] = A[i]
    for i in range(mid, size):
        R[i - mid] = A[i]
    sort(L)
    sort(R)
    merge(L, R, A)


data = ['a', 'g', 'o', 'r', 't', 'h', 'm', 's']
sort(data)
print(data)
