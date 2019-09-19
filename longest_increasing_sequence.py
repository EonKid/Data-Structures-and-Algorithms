"""
Longest increase in subsequence problem:
   find a subsequence inside the sequence which is increasing as long as possible.
   A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
"""


def lis(A: list):
    n = len(A)
    L = [1] * n
    T = []
    for i in range(0, n):
        s_pairs = set()
        for j in range(i):
            if A[j] < A[i] and L[i] < L[j] + 1:
                s_pairs.add(A[i])
                L[i] = L[j] + 1
                s_pairs.add(A[j])
        if len(s_pairs):
            T.append(s_pairs)

    print(max(L))
    print(T)


s = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
lis(s)