"""
Disjoint-set: smallest element implementation
https://www.coursera.org/learn/data-structures/lecture/EM5D0/naive-implementations

"""


class SmallestElement:

    def __init__(self, smallest: [int]):
        self.smallest = smallest

    def maketset(self, i: int):
        self.smallest[i] = i

    def find(self, i: int):
        return self.smallest[i]

    def union(self, i: int, j: int):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        m = min(i_id, j_id)
        for k in range(1, len(self.smallest)):
            if self.smallest[k] in [i_id, j_id]:
                self.smallest[k] = m

N = 12
smallest = [0] * (N+1)
disjoint_set = SmallestElement(smallest)
print("MakeSet: ")
for i in range(len(smallest)):
    disjoint_set.maketset(i)
print("Union: ")
disjoint_set.union(2, 10)
disjoint_set.union(7, 5)
disjoint_set.union(6, 1)
disjoint_set.union(3, 4)
disjoint_set.union(5, 11)
disjoint_set.union(7, 8)
disjoint_set.union(7, 3)
disjoint_set.union(12, 2)
disjoint_set.union(9, 6)
print(disjoint_set.find(6))
print(disjoint_set.find(3))
print(disjoint_set.find(11))
print(disjoint_set.find(9))

print(disjoint_set.smallest[1:N+1])
