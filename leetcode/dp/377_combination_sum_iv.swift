
// https://leetcode.com/problems/combination-sum-iv/



class Solution {
    func combinationSum4(_ nums: [Int], _ target: Int) -> Int {
         var dp = [Double](repeating: 0, count: target + 1)
         dp[0] = 1

        for x in 1 ..< dp.count{
            for num in nums{
                if x - num >= 0{
                    dp[x] += dp[x-num]
                }
            }
         }
         return Int(dp[target])
    }
}


