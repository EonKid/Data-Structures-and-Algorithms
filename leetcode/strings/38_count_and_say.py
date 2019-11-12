#!/bin/python3
# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        if n == 2: return "11"

        s = "11"

        for i in range(3, n+1):
            s += "$"
            temp = ""
            count = 1
            for j in range(1, len(s)):
                if s[j] != s[j-1]:
                    temp += str(count)
                    temp += s[j-1]
                    count = 1
                else:
                    count += 1
            s = temp

        return s



sol = Solution()
print(sol.countAndSay(6))



