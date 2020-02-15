
# https://www.coursera.org/learn/competitive-programming-core-skills/lecture/1Slx0/knapsack-without-repetitions
"""
Time comlexity: O(nW)
Space complexity: O(nW) --> O(n * logW)
"""

T = dict()


def knapsack_without_repetitions_recusrive(w: [int], v: [int], u: int, i: int):
    if (u, i) not in T:
        if i == 0:
            T[u, i] = 0
        else:
            T[u, i] = knapsack_without_repetitions_recusrive(w, v, u, i - 1)
            if u >= w[i - 1]:
                T[u, i] = max(T[u, i], knapsack_without_repetitions_recusrive(w, v, u - w[i - 1], i - 1) + v[i - 1])

    return T[u, i]


def knapsack_without_repetitions_iterative(W: int, w: [int], v: [int]):
    A = [[None] * (len(w) + 1) for _ in range(W + 1)]

    for u in range(W + 1):
        A[u][0] = 0

    for i in range(1, len(w) + 1):
        for u in range(W + 1):
            A[u][i] = A[u][i - 1]
            if u >= w[i - 1]:
                A[u][i] = max(A[u][i], A[u - w[i - 1]][i - 1] + v[i - 1])
    return A[W][len(w)]


def knapsack_without_repetitions_brute_force(W: int, w: [int], v: [int], items: [int], last: int):
    weight = sum(w[i] for i in items)
    if last == len(w) - 1:
        return sum(v[i] for i in items)
    value = knapsack_without_repetitions_brute_force(W, w, v, items, last + 1)
    if weight + w[last + 1] <= W:
        value = max(value, knapsack_without_repetitions_brute_force(W, w, v, items + [last + 1], last + 1))
    return value


w = [6, 3, 4, 2]
v = [30, 14, 16, 9]
u = 10
i = 4

print(knapsack_without_repetitions_recusrive(w, v, u, i))
print(knapsack_without_repetitions_iterative(u, w, v))
print(knapsack_without_repetitions_brute_force(u, w, v, [], -1))
