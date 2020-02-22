"""
Longest increase in subsequence problem:
   find a subsequence inside the sequence which is increasing as long as possible.
   A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
"""


def lis_sol_1(A: list):
    """
    Find LIS
    :param A:
    :return:
    """
    n = len(A)
    L = [1] * n
    for i in range(0, n):
        for j in range(i):
            if A[j] < A[i] and L[i] < L[j] + 1:
                L[i] = L[j] + 1

    print(max(L))


def lis_sol_2(A: list):
    """
    Print LIS list
    :param A:
    :return:
    """
    n = len(A)
    L = [1] * n
    prev = [-1] * n
    r = []

    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and L[i] < L[j] + 1:
                L[i] = L[j] + 1
                prev[i] = j
    last = 0
    for i in range(n):
        if L[i] > L[last]:
            last = i

    T = []
    current = last
    while current >= 0:
        T.append(current)
        current = prev[current]
    T.reverse()
    for index in T:
        r.append(A[index])
    print(r)


# brute force solution

def lis_sol_3(A: list, last_index: int) -> int:
    if last_index == -1:
        last_element = float('-inf')
    else:
        last_element = A[last_index]
    result = 0
    for i in range(last_index + 1, len(A)):
        if A[i] > last_element:
            result = max(result, 1 + lis_sol_3(A, i))
    return result



s = [8, 2, 3, 4, 5, 6, 7]



# lis_sol_1(s)
# lis_sol_2(s)
lis_sol_2(s)

