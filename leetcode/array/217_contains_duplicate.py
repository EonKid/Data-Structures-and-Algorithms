#!/bin/python3
# https://leetcode.com/problems/contains-duplicate/


class Solution:

    def containsDuplicate(self, nums: [int]) -> bool:
        if len(nums) == 0:
            return False
        T = {}
        for num in nums:
            if num not in T:
                T[num] = 1
            else:
                return True
        return False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
