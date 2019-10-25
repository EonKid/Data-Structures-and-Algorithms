#!/bin/python3


class Solution:


    def twoSum(self, nums: [int], target: int) -> [int]:
        """
        https://leetcode.com/problems/two-sum/
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param nums:
        :type nums:
        :param target:
        :type target:
        :return:
        :rtype:
        """
        has_map = {}

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in has_map:
                return [i, has_map.get(complement)]
            has_map.update({nums[i]:i})



nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
