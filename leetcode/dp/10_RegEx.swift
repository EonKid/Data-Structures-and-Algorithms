// https://leetcode.com/problems/regular-expression-matching/

class Solution {

    func isMatch(_ s: String, _ p: String) -> Bool {
             if p.count == 0{
                return s.count == 0
             }
			 var s = Array(s)
			 var p = Array(p)
             let sizeS = s.count
             let sizeP = p.count
			 var dp = Array.init(repeating: Array.init(repeating: false, count: p.count + 1), count: s.count + 1)

			 dp[0][0] = true

			 for j in 1 ... p.count{
					if  p[j - 1] == "*"{
						dp[0][j] = dp[0][j - 2]
					}
			 }

			 for i in 1 ..< sizeS + 1{
					for j in 1 ..< sizeP + 1{
						if p[j - 1] == "." || p[j - 1] == s[i - 1]{
							dp[i][j] = dp[i - 1][j - 1]
						}else if  p[j - 1] == "*" {
							dp[i][j] = dp[i][j - 2]
							if p[j - 2] == "." || p[j - 2] == s[i - 1]{
								dp[i][j] = dp[i][j] || dp[i - 1][j]
							}
						}else{
							dp[i][j] = false
						}
					}
			 }

			 return dp[s.count][p.count]
    }

}