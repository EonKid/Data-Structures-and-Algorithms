// https://leetcode.com/problems/container-with-most-water/

class Solution {

    func maxArea(_ height: [Int]) -> Int {
         if height.count == 0{
             return 0
         }
         var left = 0
			 var right = height.count - 1
			 var result = 0
			 while left < right{
						let area = (right - left) * min(height[left], height[right])
						result = max(result, area)
						if height[left] < height[right]{
						   left += 1
						}else{
							right -= 1
						}
			 }

			return result
    }

}