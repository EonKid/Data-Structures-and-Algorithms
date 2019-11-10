#!/bin/python3
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        Ts = {}
        Tr = {}
        for c in s:
            if c not in Ts:
                Ts[c] = 1
            else:
                Ts[c] = Ts[c] + 1
        for c in t:
            if c not in Tr:
                Tr[c] = 1
            else:
                Tr[c] = Tr[c] + 1

        for key in Ts:
            if key in Tr:
                if Ts[key] != Tr[key]:
                    return False
            else:
                return False
        return True


sol = Solution()
print(ord('z'))
print(sol.isAnagram("aacc" ,"ccac"))