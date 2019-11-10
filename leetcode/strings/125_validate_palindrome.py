#!/bin/python3
# https://leetcode.com/problems/valid-palindrome/
import re


class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W|_', '', s.lower())
        start_index = 0
        end_index = len(s) - 1
        while start_index < end_index:
            if s[start_index] != s[end_index]:
                return False
            start_index += 1
            end_index -= 1
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))



