
"""
https://www.coursera.org/learn/competitive-programming-core-skills/lecture/uEwXH/chain-matrix-multiplication

Time complexity: O(n*n*n)

"""

T = dict()


def matrix_mult_recursive(m: [int], i: int, j: int):
    if (i, j) not in T:
       if j == i+1:
          T[i,j] = 0
       else:
           T[i,j] = float("inf")
           for k in range(i+1, j):
               T[i,j] = min(T[i,j], matrix_mult_recursive(m, i, k) + matrix_mult_recursive(m, k, j) + m[i] * m[k] * m[j])
    return T[i,j]

def matrix_mult_iterative(m: [int]):
    n = len(m) - 1
    A = [[float("inf")] * (n+1) for _ in range(n+1)]
    for i in range(n):
        A[i][i+1] = 0
    for s in range(2, n+1):
        for i in range(n-s+1):
            j = i + s
            for k in range(i+1, j):
                A[i][j] = min(A[i][j], A[i][k]+A[k][j] + m[i] * m[k] * m[j])
    return A[0][n]


print(matrix_mult_recursive(m=[50, 20, 1, 10, 100], i=0, j=4))
print(matrix_mult_iterative(m=[50, 20, 1, 10, 100]))




 
