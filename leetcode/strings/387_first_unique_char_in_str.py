#!/bin/python3
# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        T = {}
        result = float("inf")
        if len(s) == 0:
            return -1
        for i in range(0, len(s)):
            c = s[i]
            if c not in T:
                data = [i, 1]
                T[c] = data
            else:
                data = T[c]
                data[0] = i
                data[1] = data[1] + 1
        is_min_found = False
        for key in T:
            data = T[key]
            if data[1] == 1:
                is_min_found = True
                result = min(result, data[0])
        if not is_min_found:
            return -1
        return result


sol = Solution()
print(sol.firstUniqChar("aadadaad"))