/*
https://leetcode.com/problems/maximum-product-subarray/

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
*/

class Solution {

    func maxProduct(_ nums: [Int]) -> Int {
        if nums.count == 1{
            return nums[0]
        }
        var result = nums[0]
        var leftProduct = 1
        var rightProduct = 1
        for i in 0 ..< nums.count{
            leftProduct *= nums[i]
            rightProduct *= nums[nums.count - 1 - i]
            result = max(result, leftProduct, rightProduct)
            if leftProduct == 0{
                leftProduct = 1
            }
            if rightProduct == 0{
                rightProduct = 1
            }
         }
            return result
        }

}

