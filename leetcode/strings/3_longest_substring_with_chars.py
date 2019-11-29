# python3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1
        T = {}
        i = 0
        j = 0
        result = 0
        while j < n:
            if s[j] in T:
                i = max(T[s[j]], i)
            result = max(result, j - i + 1)
            T[s[j]] = j + 1
            j += 1
        return result


sol = Solution()
s_t = "aab"
print(sol.lengthOfLongestSubstring(s_t))