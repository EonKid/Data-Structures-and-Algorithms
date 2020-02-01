"""
https://leetcode.com/problems/maximum-subarray/

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""


class Solution:
    def maxSubArray(self, nums:[int]) -> int:
        result_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], nums[i]+current_sum)
            if current_sum > result_sum:
                 result_sum = current_sum
        return result_sum


