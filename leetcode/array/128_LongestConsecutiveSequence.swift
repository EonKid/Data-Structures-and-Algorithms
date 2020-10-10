// https://leetcode.com/problems/longest-consecutive-sequence/

class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        var store = Set<Int>()
        var longestLen = 0
        for num in nums{
            store.insert(num)
        }

        for num in store{
            if !store.contains(num - 1){
                var currentNum = num
                var currentLen = 1
                while store.contains(currentNum + 1){
                    currentLen += 1
                    currentNum += 1
                }
                longestLen = max(longestLen, currentLen)
            }
        }

        return longestLen
    }
}