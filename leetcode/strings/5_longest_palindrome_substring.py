# python3
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:

    def expand_around_center(self,s: str, start: int, end: int):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if len(s) == 0:
            return ""
        if length == 1:
            return s
        result = s[0:1]
        for i in range(len(s)):
            temp_str = self.expand_around_center(s, i, i)
            if len(temp_str) > len(result):
                result = temp_str
            temp_str = self.expand_around_center(s, i, i+1)
            if len(temp_str) > len(result):
                result = temp_str
        return result


sol = Solution()
string = "babad"
print(sol.longestPalindrome(string))


