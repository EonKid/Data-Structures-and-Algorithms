// https://leetcode.com/problems/jump-game/


class Solution {
    func canJump(_ nums: [Int]) -> Bool {
         if nums.count == 0{
            return false
         }
         var currentIndex = 0
         var lastPosition = nums[currentIndex]

         while currentIndex < nums.count && currentIndex <= lastPosition{
             lastPosition = max(lastPosition, currentIndex + nums[currentIndex])
             currentIndex += 1
         }
         if currentIndex == nums.count{
            return true
         }

         return false
    }
}