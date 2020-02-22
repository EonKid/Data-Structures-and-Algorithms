/*

https://leetcode.com/problems/decode-ways/
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

*/


class Solution {

    func numDecodings(_ s: String) -> Int {
        if s.count < 1 {
            return 0
        }
        var dp = [Int](repeating: 0, count: s.count)
        let s = Array(s)
        for i in 0 ..< s.count{
            if s[i] != "0"{
                dp[i] += (i >= 1) ? dp[i-1] : 1
            }
            if i >= 1{
                let twoDigit = Int(String(s[i-1...i]))!
                if twoDigit >= 10 && twoDigit <= 26{
                    dp[i] += (i >= 2) ? dp[i-2] : 1
                }
            }
        }
        return dp[dp.count - 1]
    }

}