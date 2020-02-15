// https://leetcode.com/problems/minimum-path-sum/


class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {
        var arrResult = grid
        for i in  1 ..< arrResult[0].count{
           arrResult[0][i] += arrResult[0][i-1]
        }
        for i in 1 ..< arrResult.count{
            arrResult[i][0] += arrResult[i-1][0]
        }
        for i in 1 ..< arrResult.count{
            for j in 1 ..< arrResult[0].count{
                arrResult[i][j] = grid[i][j] + min(arrResult[i-1][j], arrResult[i][j-1])
            }
        }
        return arrResult[arrResult.count-1][arrResult[0].count-1]
    }
}