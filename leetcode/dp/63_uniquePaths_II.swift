// https://leetcode.com/problems/unique-paths-ii/

class Solution {
    func uniquePathsWithObstacles(_ obstacleGrid: [[Int]]) -> Int {
		  if obstacleGrid.count == 0 { return 0 }
           var dp = Array.init(repeating:Array.init(repeating:0, count: obstacleGrid[0].count), count: obstacleGrid.count)

		  for i in 0 ..< obstacleGrid.count{
			if obstacleGrid[i][0] != 1{
				dp[i][0] = 1
			}else{
                break
            }
		 }

		for j in 0 ..< obstacleGrid[0].count{
			if obstacleGrid[0][j] != 1{
				dp[0][j] = 1
			}else{
                break
            }
		}

		  for i in 1 ..< obstacleGrid.count{
				for j in 1 ..< obstacleGrid[0].count{
						if obstacleGrid[i][j] != 1{
								dp[i][j] = dp[i-1][j] + dp[i][j - 1]
						}else{
                            dp[i][j] = 0
                        }
				}
		  }

		  return dp[obstacleGrid.count - 1][obstacleGrid[0].count - 1]
    }
}