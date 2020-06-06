// https://leetcode.com/problems/perfect-squares/

class Solution {

    func numSquares(_ n: Int) -> Int {
          var dp = Array.init(repeating: 0, count: n + 1)
		  dp[1] = 1
		  for i in stride(from: 2, to: n + 1, by: 1){
				dp[i] = i
                var result = Int.max
                var j = 1
                while j * j <= i{
                    var nextVal = j * j
                    let remainVal = i - nextVal
                    result = min(result, dp[remainVal] + 1)
                    j += 1
                }
               dp[i] = result
		  }
		  return dp[n]
    }

}