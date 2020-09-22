// https://leetcode.com/problems/product-of-array-except-self/


class Solution {

    func productExceptSelf(_ nums: [Int]) -> [Int] {
         var size = nums.count
         var product = Array.init(repeating:0, count: size)
         var leftP = 1
         for i in stride(from:0, to: size, by: 1){
                product[i] = leftP
                leftP = leftP * nums[i]
        }

        var rightP = 1
        for i in stride(from: size - 1, to: -1, by: -1){
              product[i] = product[i] * rightP
              rightP = rightP * nums[i]
        }

		return product
    }

}