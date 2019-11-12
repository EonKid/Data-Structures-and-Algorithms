#!/bin/python3
# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        maxint = 2_147_483_647
        minint = -2_147_483_647

        x_abs = abs(x)
        result = 0
        while x_abs != 0:
            result = result * 10 + x_abs % 10
            x_abs = x_abs // 10
        if x < 0:
            result = -1 * result
        if result > maxint or result < minint:
            return 0
        return result


sol = Solution()
n = 123
print(sol.reverse(n))

