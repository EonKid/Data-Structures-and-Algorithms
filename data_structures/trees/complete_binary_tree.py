# python3
"""
Data Structure: Complete Binary Tree
https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees

Description: A binary tree is complete if all its levels are filled except
             possibly the last one which isfilled from left to right.

Height with n node: log(n)
Total nodes when l level = pow(2,l) - 1
Stored as array
Operations time complexity: O(log(n))
"""
import math


class CompleteBinaryTree:

    def __init__(self):
        self.H = []

    def size(self):
        return len(self.H)

    def get(self, i):
        return self.H[i]

    def get_max(self):
        if len(self.H) == 0:
            return None
        return self.H[0]

    def parent(self, i: int):
        return math.floor((i - 1) // 2)

    def left_child(self, i: int):
        return 2 * i + 1

    def right_child(self, i: int):
        return 2 * i + 2

    def swap(self, i, j):
        self.H[i], self.H[j] = self.H[j], self.H[i]

    def siftup(self, i: int):
        while i > 0 and self.get(self.parent(i)) < self.get(i):
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def sift_down(self, i: int):
        max_index = i
        l = self.left_child(i)
        if l <= self.size() - 1 and self.get(l) > self.get(max_index):
            max_index = l
        r = self.right_child(i)
        if r <= self.size() - 1 and self.H[r] > self.get(max_index):
            max_index = r
        if i != max_index:
            self.swap(max_index, i)
            self.sift_down(max_index)

    def insert(self, key):
        i = self.size()
        self.H.append(key)
        self.siftup(i)

    def extract_max(self):
        if self.size() == 0:
            return None
        result = self.get_max()
        self.H[0] = self.H[-1]
        del self.H[-1]
        self.sift_down(0)
        return result

    def remove_val(self,i):
        self.H[i] = float('inf')
        self.siftup(i)
        self.extract_max()

    def change_priority(self, i, p):
        old_p = self.H[i]
        self.H[i] = p
        if p > old_p:
            self.siftup(i)
        else:
            self.sift_down(i)

    def heapsort(self, alist):
        self.build_max_heap(alist)
        for i in range(len(alist) - 1, 0, -1):
            alist[0], alist[i] = alist[i], alist[0]
            self.max_heapify(alist, index=0, size=i)

    def build_max_heap(self, alist):
        length = len(alist)
        start = math.floor(length//2)
        while start >= 0:
            self.max_heapify(alist, index=start, size=length)
            start = start - 1
        self.H = alist

    def max_heapify(self,alist, index, size):
        l = self.left_child(index)
        r = self.right_child(index)
        max_index = index
        if l < size and alist[l] > alist[max_index]:
            max_index = l
        if r < size and alist[r] > alist[max_index]:
            max_index = r
        if max_index != index:
            alist[max_index], alist[index] = alist[index], alist[max_index]
            self.max_heapify(alist, max_index, size)




binary_heap = CompleteBinaryTree()
L = [3 ,2, 2, 1, 0 ,-2, 5, 7]
binary_heap.build_max_heap(L)
print(binary_heap.H)

# for num in L:
#     binary_heap.insert(num)
# print(binary_heap.H)
# print("Parent of i", binary_heap.get(binary_heap.parent(2)))
# print("Remove value at index 2")
# binary_heap.remove_val(2)
# print(binary_heap.H)
# print("change priority")
# binary_heap.change_priority(3, 50)
# print(binary_heap.H)
# print("Get max values")
# for i in range(len(binary_heap.H)):
#     max_value = binary_heap.extract_max()
#     print(max_value)




