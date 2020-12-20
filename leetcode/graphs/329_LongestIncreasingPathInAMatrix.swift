// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution {

    var result = 0
    var memo = [[Int]]()

    func dfs(_ i: Int, _ j: Int,_ matrix: [[Int]]) -> Int{
        if memo[i][j] > 0{
            return memo[i][j]
        }
        let M = matrix.count
        let N = matrix[0].count
        let dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for point in dir{
            let x = i + point[0]
            let y = j + point[1]
            if x >= 0 && y >= 0 && x < M && y < N && matrix[x][y] > matrix[i][j]{
                memo[i][j] = max(memo[i][j], dfs(x,y,matrix))
            }
        }
        memo[i][j] = memo[i][j] + 1
        return memo[i][j]
    }

    func longestIncreasingPath(_ matrix: [[Int]]) -> Int {
        let M = matrix.count
        if M == 0{
            return 0
        }
        let N = matrix[0].count
        memo = Array.init(repeating: Array.init(repeating: 0, count: N),count: M)
        for i in 0 ..< M {
            for j in 0 ..< N {
               let currentLen = dfs(i,j,matrix)
               result = max(result, currentLen)
            }
        }
        return result
    }
}