// https://leetcode.com/problems/find-the-duplicate-number/

class Solution {
    func findDuplicate(_ nums: [Int]) -> Int {
        var tortoise = nums[0]
        var hare = nums[0]

        //Phase 1
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]

        while tortoise != hare{
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
        }

        //Phase 2
        tortoise = nums[0]
        while tortoise != hare{
            tortoise = nums[tortoise]
            hare = nums[hare]
        }

        return hare
    }
}