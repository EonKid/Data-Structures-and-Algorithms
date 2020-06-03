//https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
		let n = prices.count
		if n < 2{ return 0 }
         var dpBuy = Array.init(repeating: 0, count: n)
		var dpSell = Array.init(repeating: 0, count: n)
		var dpCold = Array.init(repeating:0, count: n)

		dpBuy[0] = -prices[0]
		dpSell[0] = Int.min
		dpCold[0] = 0
		var maxPrevBuy = dpBuy[0]

		for i in stride(from: 1, to: n, by: 1){
			dpCold[i] = max(dpCold[i - 1], dpBuy[i - 1], dpSell[ i - 1])
			dpBuy[i] = dpCold[i - 1] - prices[i]
			dpSell[i] = maxPrevBuy + prices[i]
			maxPrevBuy = max(maxPrevBuy, dpBuy[i])
		}
		return max(dpSell[n - 1], dpCold[n - 1])

    }
}

