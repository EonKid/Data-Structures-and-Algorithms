#Uses python3
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

def minimum_distance(x, y):
    result = 0.
    nodes = []
    for i in range(len(x)):
        make_set(i, nodes, x, y)
    edges = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            edges.append(Edge(i, j, weight(x1=x[i], y1=y[i], x2=x[j], y2=y[j])))
    edges = sorted(edges, key= lambda edge: edge.weight)
    for edge in edges:
        if find(edge.u, nodes) != find(edge.v, nodes):
            result += edge.weight
            union(edge.u, edge.v, nodes)
    return result



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    # 4 0 0 0 1 1 0 1 1
