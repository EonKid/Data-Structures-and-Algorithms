"""

A Fenwick tree or binary indexed tree is a data structure providing efficient methods
for calculation and manipulation of the prefix sums of a table of values.

 - Space complexity for fenwick tree is O(n)
 - Time complexity to create fenwick tree is O(nlogn)
 - Time complexity to update value is O(logn)
 - Time complexity to get prefix sum is O(logn)

Reference :
        https://github.com/mission-peace/interview/blob/master/src/com/interview/tree/FenwickTree.java

"""


class BinaryIndexTree:

    def __init__(self, input: [int]):
        self.BIT = []
        self.createBinaryIndexTree(input)

    def update(self, val: int, index: int):
        print('Update BIT')
        while index < len(self.BIT):
            self.BIT[index] += val
            index = self.getNext(index)

    def getSum(self, index: int):
        print('Get sum of first index elements')
        index += 1
        sum = 0
        while index > 0:
            sum += self.BIT[index]
            index = self.getParent(index)
        return sum

    def getNext(self, index: int):
        return index + (index & -index)

    def getParent(self, index: int):
        return index - (index & -index)

    def createBinaryIndexTree(self, input: [int]):
        self.BIT = [0] * (len(input) + 1)
        for i in range(1,  len(input)+1):
            self.update(input[i  - 1], i)
        print('Binary Index Tree:')
        print(self.BIT)


input_data = [1,2,3,4,5,6,7]
tree = BinaryIndexTree(input=input_data)
print(tree.getSum(4))
