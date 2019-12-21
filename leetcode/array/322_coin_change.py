# python3
# https://leetcode.com/problems/coin-change/

"""
Video explanation: https://www.youtube.com/embed/18NVyOI_690
"""


class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # base case
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        if dp[amount] > amount:
            return -1
        return dp[amount]

