// https://leetcode.com/problems/coin-change/


class Solution {
    func coinChange(_ coins: [Int], _ amount: Int) -> Int {
        var dp = Array.init(repeating:amount+1, count: amount+1)
        dp[0] = 0

        for coin in coins{
           for x in coin ..< amount + 1{
               dp[x] = min(dp[x], dp[x - coin] + 1)
          }
        }

        if dp[amount] > amount{
            return -1
        }
        return dp[amount]
    }
}