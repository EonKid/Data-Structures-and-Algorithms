#!/bin/python3
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
# row = i + 3 * (sub // 3)
# col = j + 3 * (sub % 3)


class Solution:

    def isValidSudoku(self, board: [[str]]) -> bool:
        row_count = {}
        col_count = {}
        grid_count = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] is not '.':

                    # check row count
                    if board[i][j] in row_count and i in row_count[board[i][j]]:
                        return False
                    else:
                        row_count[board[i][j]] = row_count.get(board[i][j], []) + [i]

                    # check colum count
                    if board[i][j] in col_count and j in col_count[board[i][j]]:
                        return False
                    else:
                        col_count[board[i][j]] = col_count.get(board[i][j], []) + [j]

                    # check grid
                    grid_value = 3*(i//3)+j//3
                    if board[i][j] in grid_count and grid_value in grid_count[board[i][j]]:
                        return False
                    else:
                        grid_count[board[i][j]] = grid_count.get(board[i][j], []) + [grid_value]

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