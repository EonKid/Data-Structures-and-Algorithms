#!/bin/python3
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/
"""

Time complexity: O(n)
Space complexity: O(1)

"""


class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits




num_list = [4,3,2,9]
sol = Solution()
print(sol.plusOne(num_list))
