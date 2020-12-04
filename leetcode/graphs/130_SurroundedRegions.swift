// https://leetcode.com/problems/surrounded-regions/


/*

X X X X
X O O X
X X O X
X O X X


*/

class Solution {

    func dfs(_ board: inout [[Character]],_ i: Int,_ j: Int, _ m: Int, _ n: Int){
		board[i][j] = "*"
 		var directions: [[Int]] = [[1, 0], [-1, 0], [0, 1], [0, -1]]
		for point in directions{
		    var x = i + point[0]
		    var y = j + point[1]
		    if x < 0 || x >= m || y < 0 || y >= n || board[x][y] != "O"{
				continue
		    }
		    dfs(&board, x, y, m, n)
		}

    }

    func solve(_ board: inout [[Character]]) {

		let m = board.count
		if m == 0{ return }
		let n = board[0].count

		// check rows and run dfs
          for i in stride(from: 0, to: m, by: 1){
				//first col
				if board[i][0] == "O"{
					dfs(&board, i, 0,m, n)
				}
				//last col
				if board[i][n - 1] == "O"{
					dfs(&board, i, n - 1, m, n)
				}
		}

		//check columns and run dfs
		for j in stride(from: 0, to: n, by: 1){
			// first row
			if board[0][j] == "O"{
				dfs(&board, 0, j, m, n)
			}

			// last col
			if board[m - 1][j] == "O"{
				dfs(&board, m - 1, j, m, n)
			}

		}

		// convert "*" to "O" and remaining "O" to "X"

		for i in stride(from: 0, to: m, by: 1){
			for j in stride(from: 0, to: n, by: 1){
				if board[i][j] == "*"{
					board[i][j] = "O"
				}else {
					board[i][j] = "X"
				}
			}

		}


    }
}




