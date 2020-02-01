
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Input : [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

"""


class Solution:
    def maxProfit(self, prices:[int]) -> int:
        slow_pointer = 0
        profit = 0
        for fast_pointer in range(slow_pointer+1, len(prices)):
            if prices[slow_pointer] > prices[fast_pointer]:
                 slow_pointer = fast_pointer
            profit = max(profit, prices[fast_pointer]-prices[slow_pointer])
        return profit
