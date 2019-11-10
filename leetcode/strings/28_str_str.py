#!/bin/python3
# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(needle) > 0 and len(haystack) == 0: return -1
        if len(haystack) < len(needle): return -1
        if len(haystack) == 1 and len(needle) and haystack[0] == needle[0]: return 0
        result = -1
        is_found = False
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0] and i != len(haystack) - 1:
                is_found = True
                for j in range(1, len(needle)):
                    if i + j < len(haystack):
                        if haystack[j + i] != needle[j]:
                            is_found = False
                            break
                    else:
                        return -1

            if is_found:
                result = i
                return result
            is_found = False

        return result


sol = Solution()
haystack = "a"
needle = "a"
print(sol.strStr(haystack, needle))

