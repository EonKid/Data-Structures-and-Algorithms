"""

Binary Search
https://www.coursera.org/learn/algorithmic-toolbox/lecture/vKN0b/binary-search-runtime
Time complexity: log(n) + c

"""

import math


def binary_search(A, key):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = math.floor(low + (high - low) / 2)
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None

nums = [3, 5, 8, 10, 12, 15, 18, 20, 20, 50, 60]
print(binary_search(nums, 100))




