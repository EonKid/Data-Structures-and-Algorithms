# Uses python3
import sys
import math


# Kruskal algorithm

class Node:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.parent = c
        self.rank = 0


class Edge:
    def __init__(self, a, b, c):
        self.u = a
        self.v = b
        self.weight = c


def make_set(i, nodes, x, y):
    nodes.append(Node(x[i], y[i], i))


def weight(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def find(i, nodes):
    if i != nodes[i].parent:
        nodes[i].parent = find(nodes[i].parent, nodes)
    return nodes[i].parent


def union(u, v, nodes):
    r1 = find(u, nodes)
    r2 = find(v, nodes)
    if r1 != r2:
        if nodes[r1].rank > nodes[r2].rank:
            nodes[r2].parent = r1
        else:
            nodes[r1].parent = r2
            if nodes[r1].rank == nodes[r2].rank:
                nodes[r2].rank += 1


def clustering(x, y, k):
    nodes = []
    for i in range(len(x)):
        make_set(i, nodes, x, y)
    edges = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            edges.append(Edge(i, j, weight(x1=x[i], y1=y[i], x2=x[j], y2=y[j])))
    edges = sorted(edges, key=lambda edge: edge.weight)
    union_count = 0
    for edge in edges:
        if find(edge.u, nodes) != find(edge.v, nodes):
            union_count += 1
            union(edge.u, edge.v, nodes)
        if union_count > n - k:
            return edge.weight
    return -1.


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input().split()))
    # n = data[0]
    # data = data[1:]
    # x = data[0:2 * n:2]
    # y = data[1:2 * n:2]
    # data = data[2 * n:]
    # k = data[0]
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    k = int(input())
    print("{0:.9f}".format(clustering(x, y, k)))
    # 1 2 7 6 4 3 5 1 1 7 2 7 5 7 3 3 7 8 2 8 4 4 6 7 2 6 3
