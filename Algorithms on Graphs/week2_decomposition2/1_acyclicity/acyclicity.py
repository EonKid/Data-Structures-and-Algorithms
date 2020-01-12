#Uses python3

import sys

def dfs(v, visited, recur_stack, adj):
    visited[v] = True
    recur_stack[v] = True
    for node in adj[v]:
        if visited[node] == False:
            if dfs(node, visited, recur_stack, adj) == True:
                return True
        elif recur_stack[node] == True:
            return True
    recur_stack[v] = False
    return False

def acyclic(adj):
    visited = [0]*(len(adj))
    recur_stack = [0]*(len(adj))
    for v in range(len(adj)):
        if visited[v] == False:
            if dfs(v, visited, recur_stack, adj):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
    # 4 4 1 2 4 1 2 3 3 1
    # 5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5