# Uses python3
import sys


def optimal_weight(W, w):
    n = len(w)
    T = [[0] * (n+1) for _ in range(W+1)]
    for i in range(1, n+1):
        for u in range(W+1):
            T[u][i] = T[u][i-1]
            if w[i-1] <= u:
                T[u][i] = max(T[u - w[i-1]][i-1] + w[i-1], T[u][i])
    return T[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
