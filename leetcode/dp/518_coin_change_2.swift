// https://leetcode.com/problems/coin-change-2/



class Solution {

    func change(_ amount: Int, _ coins: [Int]) -> Int {
        if amount == 0 {
            return 1
        }
        var dp  = Array.init(repeating: 0, count: amount+1)
            dp[0] = 1
            for coin in coins{
                var x = coin
                while x < amount + 1 {
                    dp[x] += dp[x - coin]
                    x += 1
                }
            }
        return dp[amount]

    }

}