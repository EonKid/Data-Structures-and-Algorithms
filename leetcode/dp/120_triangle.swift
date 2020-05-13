// https://leetcode.com/problems/triangle/

class Solution {
    func minimumTotal(_ triangle: [[Int]]) -> Int {
         if triangle.count == 0{
             return 0
         }
         let n = triangle.count
         var dp = triangle[n - 1]
         for row in stride(from: n - 2, to: -1, by: -1){
             for col in stride(from: 0, to: row + 1, by: 1){
                 dp[col] = triangle[row][col] + min(dp[col], dp[col+1])
             }
         }
         return dp[0]
    }
}