
// https://leetcode.com/problems/repeated-substring-pattern/submissions/

import Foundation

class Solution {
    
    func computeLCSArray(s: NSString, M: Int, lps:[Int])->[Int]{
        var length = 0
        var i = 1
        var lps = lps
        while(i < M){
            if s.character(at: i) == s.character(at: length){
                length += 1
                lps[i] = length
                i += 1
            }else{
                if length != 0{
                    length = lps[length-1]
                }else{
                    lps[i] = 0
                    i += 1
                }
            }
        }
        return lps
    }
    
    func repeatedSubstringPattern(_ s: String) -> Bool {
        let s = (s as NSString)
        let n = s.length
        var lps = [Int](repeating:0,count: n)
        lps = computeLCSArray(s: s, M: n, lps: lps)
        let len = lps[n-1]
        if len > 0 && n % (n - len) == 0{
            return true
        }else{
            return false
        }
    }
}


let sol = Solution()
let string = "aba"
print(sol.repeatedSubstringPattern(string))



