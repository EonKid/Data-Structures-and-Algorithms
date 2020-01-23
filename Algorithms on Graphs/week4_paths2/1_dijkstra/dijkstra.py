#Uses python3

import sys
import queue
from functools import total_ordering

@total_ordering
class Node(object):

    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __eq__(self, other):
        return ((self.distance, self.index) == (other.distance, other.index))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.distance, self.index) < (other.distance, other.index))

    def __repr__(self):
        return "%d %d" % (self.index, self.distance)


def distance(adj, cost, s, t):
    dist = [float('inf')]*len(adj)
    dist[s] = 0
    priority_queue = queue.PriorityQueue()
    priority_queue.put(Node(s, dist[s]))

    while not priority_queue.empty():
        node = priority_queue.get()
        for v in adj[node.index]:
            if dist[v] > dist[node.index] + cost[node.index][adj[node.index].index(v)]:
                dist[v] = dist[node.index] + cost[node.index][adj[node.index].index(v)]
                priority_queue.put(Node(v, dist[v]))
    if dist[t] == float('inf'):
        return -1
    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
    # 4 4 1 2 1 4 1 2 2 3 2 1 3 5 1 3
    # 5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 1 5
