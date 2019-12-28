#!/bin/python3

"""
Quicksort

- Sort list by selecting pivot
- Partition list
- Arranging element smaller than pivot to left of pivot
- Arranging element greater than pivot to right of pivot

Time space complexity

Best case: n * log(n)
Average case: n * log(n)
Worst case: O(n * n)

Space complexity: log(n)
"""


def partition_list(A, start_index, end_index):
    pivot = A[end_index]
    partition_index = start_index
    for i in range(start_index, end_index):
        if A[i] <= pivot:
            A[i], A[partition_index] = A[partition_index], A[i]
            partition_index += 1
    A[partition_index], A[end_index] = A[end_index], A[partition_index]
    return partition_index


def sort(A, start_index, end_index):
    if start_index < end_index:
        partition_index = partition_list(A, start_index, end_index)
        sort(A, start_index, partition_index-1)
        sort(A, partition_index+1, end_index)


data = [2, 4, 1, 6, 8, 5, 3, 7]
sort(data, 0, len(data)-1)
print(data)