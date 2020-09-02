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

    }

