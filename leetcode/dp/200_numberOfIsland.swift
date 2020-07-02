// https://leetcode.com/problems/number-of-islands/


class Solution {

    func numIslands(_ grid: [[Character]]) -> Int {
		  if grid.count == 0{ return 0 }
            var visited = Array.init(repeating: Array.init(repeating: false, count: grid[0].count), count: grid.count)
            var directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            var result = 0
			for row in stride(from: 0, to: grid.count, by: 1){
				for col in stride(from: 0, to: grid[0].count, by: 1){
					  if !visited[row][col] && grid[row][col] == Character("1"){
							result += 1
							self.dfs(&visited, grid, directions, row, col)
					  }
				}
			}

			return result
    }

	func isWithinBounds(_ grid: [[Character]], _ row: Int, _ col: Int) -> Bool{
			return row >= 0 && col >= 0 && row < grid.count && col < grid[0].count
	}

	func dfs(_ visited: inout [[Bool]], _ grid: [[Character]], _ directions: [[Int]], _ row: Int,_ col: Int){

       if grid[row][col] != Character("1") { return }


            visited[row][col] = true


			 for dir in directions{
				let row_dir = row + dir[0]
				let col_dir = col + dir[1]

                    if self.isWithinBounds(grid, row_dir, col_dir) && !visited[row_dir][col_dir] && grid[row_dir][col_dir] == Character("1"){
                        self.dfs(&visited, grid, directions, row_dir, col_dir)
                    }


			}
	}

}