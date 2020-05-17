// https://leetcode.com/problems/triangle/

class Solution {

    func minimumTotal(_ triangle: [[Int]]) -> Int {

        func sol2() -> Int{
          if triangle.count == 0{ return 0 }
           var prevRow = triangle[0]
		   for i in stride(from: 1, to: triangle.count, by: 1){
				var currRow = triangle[i]
				currRow[0] = currRow[0] + prevRow[0]
                  for j in stride(from: 1, to: currRow.count - 1, by: 1){
							currRow[j] = currRow[j] + min(prevRow[j-1], prevRow[j])
				}
                currRow[currRow.count - 1] = currRow[currRow.count - 1] + prevRow[prevRow.count - 1]
				prevRow = currRow
		  }
           return prevRow.min() ?? 0
        }

        func sol1() -> Int{
            let n = triangle.count
            if n == 0{ return 0 }
            var dp = triangle[n - 1]
            for row in stride(from: triangle.count - 2, to: -1, by: -1){
                for col in stride(from: 0, to: row + 1, by: 1){
                    dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
                }
            }
            return dp[0]
        }
        return sol1()
    }

}


