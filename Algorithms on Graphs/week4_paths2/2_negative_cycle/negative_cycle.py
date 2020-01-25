#Uses python3

import sys


def negative_cycle(adj, cost):
    dist = [-1] * len(adj)
    dist[0] = 0
    for i in range(len(adj)):
        for u in range(len(adj)):
            for index, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][index]:
                    dist[v] = dist[u] + cost[u][index]
        if i == len(adj) - 2:
            dist2 = list(dist)
        if i == len(adj) - 1:
            dist1 = list(dist)
    if dist2 == dist1:
        return 0
    else:
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
    # 4 4 1 2 -5 4 1 2 2 3 2 3 1 1
    # 10 9 1 2 1 6 7 1 8 9 1 9 10 1 3 4 1 7 8 1 4 5 1 5 6 1 2 3 1
