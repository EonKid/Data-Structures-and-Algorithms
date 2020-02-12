"""
https://leetcode.com/problems/trapping-rain-water/
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height: [int]) -> int:
        if len(height) == 0: return 0
        water_trapped = 0
        left = 0
        left_max = 0
        n = len(height)
        right = n - 1
        right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
