#!/bin/python3
# https://leetcode.com/problems/plus-one/
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
