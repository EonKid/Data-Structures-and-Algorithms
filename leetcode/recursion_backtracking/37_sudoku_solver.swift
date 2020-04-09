// https://leetcode.com/problems/sudoku-solver/


class Solution {


	func unAssignedInGrid(_ board: [[Character]], _ rowStart: Int, _ colStart: Int, _ num: Character) -> Bool{
			for row in 0 ..< 3{
					for col in 0 ..< 3{
							if board[row+rowStart][col+colStart] == num{
								return false
							}
					}
			}
			return true
	}

	func unAssignedInCol(_ board: [[Character]], _ col: Int, _ num: Character) -> Bool{
			for row in 0 ..< board.count{
				  if board[row][col] == num{
						return false
				  }
			}
			return true
	}

	func unAssignedInRow(_ board: [[Character]], _ row: Int, _ num: Character ) -> Bool{
			for col in 0 ..< board.count{
					if board[row][col] == num{
						return false
					}
			}
			return true
	}

	func isSafe(_ board: [[Character]], _ row: Int, _ col: Int, _ num: Int) -> Bool{
            var number : Character = Character(String(num))

			return unAssignedInRow(board, row, number) && unAssignedInCol(board, col, number) && unAssignedInGrid(board, row - row % 3, col - col % 3, number)
	}

	func notAssignedConfigurations(_ board: [[Character]],_ row: inout Int?, _ col: inout Int?) -> Bool{
			for i in 0 ..< board.count{
					for j in 0 ..< board.count{
							if board[i][j] == "."{
									row = i
									col = j
									return true
							}
					}
			}
			return false
	}


	func solve(_ board: inout [[Character]]) -> Bool{
			var row: Int?
			var col: Int?
			if !notAssignedConfigurations(board, &row, &col){
					return true
			}
			for num in 1 ..< 10{
					if isSafe(board, row!, col!, num){
						board[row!][col!] = Character(String(num))
						if solve(&board){
                            return true
                        }
                        board[row!][col!] = Character(String("."))
					}
			}
        return false

	}

    func solveSudoku(_ board: inout [[Character]]) {
           if solve(&board){
               print("solved")
           }

    }

}