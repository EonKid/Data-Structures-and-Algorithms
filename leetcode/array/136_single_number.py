#!/bin/python3
# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        result = 0
        for num in nums:
            result ^= num
            print(num, result)

        return result


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))

