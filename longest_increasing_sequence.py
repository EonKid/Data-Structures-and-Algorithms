"""
Longest increase in subsequence problem:
   find a subsequence inside the sequence which is increasing as long as possible.
   A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
"""


def lis(A: list):
    n = len(A)
    L = [1] * n
    for i in range(0, n):
        for j in range(i):
            if A[j] < A[i] and L[i] < L[j] + 1:
                L[i] = L[j] + 1
    print(max(L))


s = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
lis(s)