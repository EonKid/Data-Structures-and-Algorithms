#!/bin/python3
# https://leetcode.com/problems/reverse-string/

class Solution():
    def reverseString(self, s: [str]) -> None:
        start_index = 0
        end_index = len(s) - 1
        if end_index is -1:
            return None

        while start_index < end_index:
              s[start_index], s[end_index] = s[end_index], s[start_index]
              start_index += 1
              end_index -= 1

sol = Solution()
string = ["h","e","l","l","o"]
sol.reverseString(string)
     





