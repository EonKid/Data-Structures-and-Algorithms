#!/bin/python3
# https://leetcode.com/problems/two-sum/

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
        value_index_map = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in value_index_map:
                return [i, value_index_map.get(complement)]
            value_index_map.update({nums[i]:i})

nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))

