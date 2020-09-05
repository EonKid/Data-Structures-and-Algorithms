// https://leetcode.com/problems/wildcard-matching/

    class Solution {

        func isMatch(_ s: String, _ p: String) -> Bool {
                    var s = Array(s)
                    var p = Array(p)
                    let sizeS = s.count
                    let sizeP = p.count
                    var i = 0
                    var j = 0
                    var lsp = -1
                    var lss = -1

                    while j < sizeS {
                        if  i < sizeP && p[i] == "*"{
                                i += 1
                                lsp = i
                                lss = j
                        }else if i < sizeP && j < sizeS && p[i] == s[j] || i < sizeP && j < sizeS && p[i] == "?"{
                                i += 1
                                j += 1
                        }else{
                                if lsp == -1{
                                    return false
                                }
                                i = lsp
                                lss += 1
                                j = lss

                        }
                    }
                    while i < sizeP && p[i] == "*" {
                        i += 1
                    }
                    return i == sizeP
        }


        func memo(_ s: [Character], _ p: [Character]) -> Bool{
            if p.count == 0{ return s.count == 0  }
            var sizeS = s.count
            var sizeP = p.count
            var dp = Array.init(repeating: Array.init(repeating: false, count: sizeP + 1), count: sizeS + 1)
            dp[0][0] = true


            //fill for *
            for j in 1 ... sizeP{
                if p[j - 1] == "*" {
                dp[0][j] = dp[0][j - 1]
                }
            }

            if s.count == 0{
                return dp[0][p.count]
            }

            for i in 1 ... sizeS{
                for j in 1 ... sizeP {
                    if s[i - 1] == p[j - 1] || p[j - 1] == "?"{
                        dp[i][j] = dp[i - 1][j  - 1]
                    }
                    if p[j - 1] == "*"{
                        dp[i][j] = dp[i - 1][j] || dp[i][j - 1] || dp[i - 1][j - 1]
                    }
                }
            }
            return dp[sizeS][sizeP]
        }



    }

