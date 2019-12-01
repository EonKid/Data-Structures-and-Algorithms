# python3
# https://leetcode.com/problems/repeated-substring-pattern/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        data = (s+s)[1:-1]
        return s in data


sol = Solution()
string = "abab"
print(sol.repeatedSubstringPattern(string))
