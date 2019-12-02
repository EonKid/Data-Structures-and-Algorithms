// https://leetcode.com/problems/longest-continuous-increasing-subsequence/


class Solution {
    func findLengthOfLCIS(_ nums: [Int]) -> Int {
        var right = 0
        var result = 0
        for left in 0 ..< nums.count{
            if left > 0 && nums[left-1] >= nums[left]{
                right = left
            }
            result = max(result,left-right+1)
        }
        return result
    }
}

let L =  [1,3,5,4,7]
let sol = Solution()
print(sol.findLengthOfLCIS(L))
