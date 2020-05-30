"""
https://leetcode.com/problems/pascals-triangle/

"""


class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows == 0: return []
        n = numRows - 1
        cache = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(n + 1):
            cache[i][0] = 1
        for i in range(n + 1):
            cache[i][i] = 1
        result = []
        result.append([cache[0][0]])
        for i in range(1, n + 1):
            data = []
            data.append(cache[i][0])
            for j in range(1, i + 1):
                cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]
                data.append(cache[i][j])
            result.append(data)
        return result

