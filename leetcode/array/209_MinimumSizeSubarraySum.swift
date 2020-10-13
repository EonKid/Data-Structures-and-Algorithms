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

func longestSubstringKDistinct(_ s: String, _ k: Int) -> Int {

    if s.count == 0 || s.count < k{
        return -1
    }

    // s = "aabbcc" k = 2
    // map = []
    var map = [Character: Int]()
    var maxLen = Int.min
    var windowStart = 0
    let s = Array(s)
    for windowEnd in stride(from: 0, to: s.count, by: 1){
        let rightChar = s[windowEnd]
        if let charCount = map[rightChar]{
            map[rightChar] = charCount + 1
        }else{
            map[rightChar] = 1
        }

        while map.count > k {
            let leftChar = s[windowStart]
            if let charCount = map[leftChar]{
                map[leftChar] = charCount - 1
            }
            if let cCount = map[leftChar] {
                if cCount == 0{
                    map.removeValue(forKey: leftChar)
                }
            }
            windowStart += 1
        }
        maxLen = max(maxLen, windowEnd - windowStart + 1)
    }
    return maxLen
}

print("Longest substring: \(longestSubstringKDistinct("aaabbb", 3))")



print(findMaxSumSubarray([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))