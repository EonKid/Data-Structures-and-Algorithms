#!/bin/python3
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        buy_pointer = 0
        max_profit = 0
        for sell_pointer in range(1, len(prices)):
            if prices[buy_pointer] < prices[sell_pointer]:
                profit = prices[sell_pointer] - prices[buy_pointer]
                max_profit += profit
            buy_pointer += 1
        return max_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
