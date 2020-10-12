// https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution {
    func minSubArrayLen(_ s: Int, _ nums: [Int]) -> Int {
         var minWinSize = Int.max
         var windowStart = 0
         var currentSum = 0

         for windowEnd in stride(from: 0, to: nums.count, by: 1){
             currentSum += nums[windowEnd]
             while currentSum >= s{
                 minWinSize = min(minWinSize, windowEnd - windowStart + 1)
                 currentSum -= nums[windowStart]
                 windowStart += 1
             }
         }
         return minWinSize == Int.max ? 0 : minWinSize
    }
}

func findMaxSumSubarray(_ nums: [Int], _ k: Int) -> Int{
    var maxSum = Int.min
    var currentSum = 0

    for i in stride(from: 0, to: nums.count, by: 1){
        currentSum += nums[i]
        if i >= k - 1{
            maxSum = max(currentSum, maxSum)
            currentSum -= nums[i - (k - 1)]
        }
    }

    return maxSum

}



print(findMaxSumSubarray([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))