"""
https://leetcode.com/problems/word-break-ii/

DFS + memoization solution

"""


class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        def dfs(s, wordDict, memo):
            if s in memo:
                return memo[s]
            result = []
            if len(s) == 0:
                return result
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(s) == len(word):
                    result.append(word)
                else:
                    sub_list = dfs(s[len(word):], wordDict, memo)
                    for item in sub_list:
                        item = word + " " + item
                        result.append(item)
            memo[s] = result
            return result

        memo = {}
        return dfs(s, wordDict, memo)















