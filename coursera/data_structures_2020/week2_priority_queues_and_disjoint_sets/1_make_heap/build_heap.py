# python3
from math import floor


class MinHeapBuilder:

    def __init__(self):
        self.swaps = []
        self.data = []

    @property
    def size(self):
        return len(self.data)

    def left_child(self, i: int):
        return 2 * i + 1

    def right_child(self, i: int):
        return 2 * i + 2

    def sift_down(self, i: int):
        l = self.left_child(i)
        r = self.right_child(i)
        min_index = i

        if l <= self.size - 1 and self.data[l] < self.data[min_index]:
            min_index = l
        if r <= self.size - 1 and self.data[r] < self.data[min_index]:
            min_index = r
        if i != min_index:
            self.swaps.append((i, min_index))
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.sift_down(min_index)

    def build_heap(self):
        """Build a heap from ``data`` inplace.

        Returns a sequence of swaps performed by the algorithm.
        """
        start = floor(len(self.data) // 2)
        while start >= 0:
            self.sift_down(start)
            start -= 1
        return self.swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    heap = MinHeapBuilder()
    heap.swaps = []
    heap.data = data
    swaps = heap.build_heap()

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
