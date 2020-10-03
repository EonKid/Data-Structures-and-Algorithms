// https://leetcode.com/problems/game-of-life/


class Solution {
    func gameOfLife(_ board: inout [[Int]]) {

         let rowCount = board.count
		 let colCount = board[0].count

		var result = Array.init(repeating: Array.init(repeating: 0, count: colCount), count: rowCount)
        print(result)

			var directions = [[-1, 0], [-1,1], [0, 1],
                             [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

			for i in stride(from: 0, to: rowCount, by: 1){
					for j in stride(from: 0, to: colCount, by: 1){
								var liveCount = 0
								for dir in directions{
										let x = i + dir[0]
										let y = j + dir[1]
										if x >= 0 && x < rowCount && y >= 0 && y < colCount && board[x][y] == 1{
											liveCount += 1
										}
								}
								if board[i][j] == 0 && liveCount == 3{
										result[i][j] = 1
								}else if board[i][j] == 1{
											if liveCount == 2 || liveCount == 3{
												result[i][j] = 1
											}
								}

						}

			}

			for i in stride(from: 0, to: rowCount, by: 1){
					for j in stride(from: 0, to: colCount, by: 1){
								board[i][j] = result[i][j]
						}

			}


    }
}