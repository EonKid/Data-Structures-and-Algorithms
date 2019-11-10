#!/bin/python3
# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        slow_pointer = 0
        for fast_pointer in range(0, len(nums)):
            if nums[fast_pointer] != 0 and slow_pointer < len(nums):
                nums[slow_pointer], nums[fast_pointer] = nums[fast_pointer], nums[slow_pointer]
                slow_pointer += 1

        print(nums)

sol = Solution()
n = [0,1,0,3,12]
sol.moveZeroes(n)