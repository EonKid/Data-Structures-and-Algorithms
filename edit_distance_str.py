#!/bin/python3
# https://www.youtube.com/watch?v=Xxx0b7djCrs
#https://www.coursera.org/learn/competitive-programming-core-skills/lecture/slwRn/algorithm


T = dict()


def edit_distance_iterative(a: str, b: str):
    A = [ [float("inf")] * (len(b) + 1) for _ in range(len(a) + 1) ]
    
    for i in range(len(a)+1):
        A[i][0] = i
    
    for j in range(len(b)+1):
        A[0][j] = j
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            diff = 0 if a[i-1] == b[j-1] else 1
            A[i][j] = min(A[i][j-1]+1, A[i-1][j]+1, A[i-1][j-1]+diff)

    return A[len(a)][len(b)]
    

def edit_distance(a: str, b: str, i: int, j: int) -> int:
    if (i, j) not in T:
        if i == 0: T[i,j] = j
        elif j == 0: T[i,j] = i
        else:
           diff = 0 if a[i-1] == b[j-1] else 1
           T[i, j] = min(edit_distance(a,b,i,j-1)+1, edit_distance(a,b,i-1, j)+1, edit_distance(a,b,i-1,j-1) + diff)

    return T[i, j]


m = "distance"
n = "editing"
print("Recursive solution: ",edit_distance(m, n, len(m), len(n)))
print("Iterative solution: ", edit_distance_iterative(m, n))