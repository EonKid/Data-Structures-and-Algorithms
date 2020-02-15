"""
Disjoint-sets: Path Compression
https://www.coursera.org/learn/data-structures/lecture/Q9CVI/path-compression
Iterated logarithm , log * (n)
"""


class PathCompression:

    def __init__(self, parent: [int]):
        self.parent = parent
        n = len(self.parent)
        self.rank = [0]*(n+1)

    def maketset(self, i: int):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i: int):
        while i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
            i = self.parent[i]
        return self.parent[i]

    def union(self, i: int, j: int):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[j_id] + 1

N = 60
parent = [0] * (N+1)
disjoint_set = PathCompression(parent=parent)
print("MakeSet: ")
for i in range(len(parent)):
    disjoint_set.maketset(i)
for i in range(30):
    disjoint_set.union(i, 2 * i)
for i in range(20):
    disjoint_set.union(i, 3 * i)
for i in range(12):
    disjoint_set.union(i, 5 * i)
for i in range(60):
    disjoint_set.find(i)

# disjoint_set.union(2,4)
# disjoint_set.union(5, 2)
# disjoint_set.union(3, 1)
# disjoint_set.union(2, 3)
# disjoint_set.union(2, 6)
print(disjoint_set.parent[1:N+1])
print(max(disjoint_set.rank[1:N+1]))