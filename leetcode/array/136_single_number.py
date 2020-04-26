#!/bin/python3
# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        result = 0
        for num in nums:
            print(num, result)
            result ^= num


        return result


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))

