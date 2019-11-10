#!/bin/python3
# https://leetcode.com/problems/rotate-array/
# [ <first element to include> : <first element to exclude> : <step> ]

class Solution:

    def reverse_list(self, A: [int], start: int, end: int):
        while start < end:
            temp = A[start]
            A[start] = A[end]
            A[end] = temp
            start += 1
            end -= 1

    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        To slice a list, there's a simple syntax: array[start:stop:step]
        You can omit any parameter. These are all valid: array[start:], array[:stop], array[::step]

        """
        k = k % len(nums)
        n = len(nums)
        if k == 0: return
        self.reverse_list(nums, 0, len(nums)-1)
        self.reverse_list(nums, 0, k-1)
        self.reverse_list(nums, k, n-1)

sol = Solution()
sol.rotate([1,2,3,4,5,6,7], 3)