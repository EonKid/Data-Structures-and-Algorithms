#!/bin/python3
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))


