#!/bin/python3
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
# row = i + 3 * (sub // 3)
# col = j + 3 * (sub % 3)


class Solution:

    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        grid = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] is not '.':
                    num = board[i][j]
                    # check grid
                    grid_value = 3*(i//3)+j//3

                    if num in rows[i] or num in columns[j] or num in grid[grid_value]:
                        return False
                    else:
                        rows[i].add(num)
                        columns[j].add(num)
                        grid[grid_value].add(num)

        return True




sol = Solution()
L = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(sol.isValidSudoku(L))


