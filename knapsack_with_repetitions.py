# https://www.coursera.org/learn/competitive-programming-core-skills/lecture/1cjXH/knapsack-with-repetitions

T = dict()


def knapsack_recursive(w: [int], v: [int], u: int) -> int:
    if u not in T:
       T[u] = 0
    for i in range(len(w)):
        if w[i] <= u:
           T[u] = max(T[u], knapsack_recursive(w, v, u - w[i]) + v[i])
    return T[u]


def knapsack_iterative(w: [int], v: [int], W: int):
    A = [0] * (W+1)
    
    for u in range(1, W+1):
        for i in range(len(w)):
            if w[i] <= u:
               A[u] = max(A[u], A[u - w[i]] + v[i])
    return A[W]


def knapsack_brute_force(w: [int], v: [int], W: int, items: [int]):
    weight = sum(w[i] for i in items)
    value = sum(v[i] for i in items)

    for i in range(len(w)):
        if weight+w[i] <= W:
           value = max(value, knapsack_brute_force(w, v, W, items + [i]))

    return value



w = [6, 3, 4, 2]
v = [30, 14, 16, 9]
u = 10

print(knapsack_recursive(w, v, u))
print(knapsack_iterative(w, v, u))
print(knapsack_brute_force(w, v, u,[]))














