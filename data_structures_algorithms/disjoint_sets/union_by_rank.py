"""
Disjoint-sets
https://www.coursera.org/learn/data-structures/lecture/qb4c2/union-by-rank
Height: log(n)
Tree of height k have pow(2, k) nodes
"""


class UnionByRank:

    def __init__(self, parent: [int]):
        self.parent = parent
        n = len(self.parent)
        self.rank = [0]*(n+1)

    def maketset(self, i: int):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i: int):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

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

N = 12
parent = [0] * (N+1)
disjoint_set = UnionByRank(parent=parent)
print("MakeSet: ")
for i in range(len(parent)):
    disjoint_set.maketset(i)
print("Union: ")
disjoint_set.union(2,10)
disjoint_set.union(7, 5)
disjoint_set.union(6, 1)
disjoint_set.union(3, 4)
disjoint_set.union(5, 11)
disjoint_set.union(7, 8)
disjoint_set.union(7, 3)
disjoint_set.union(12, 2)
disjoint_set.union(9, 6)

print(disjoint_set.parent[1:N+1])
print(disjoint_set.rank[1:N+1])

