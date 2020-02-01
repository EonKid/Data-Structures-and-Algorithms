"""
https://leetcode.com/problems/trapping-rain-water/
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height: [int]) -> int:
        if len(height) == 0:
            return 0
        water_trapped = 0
        L = [0]*len(height)
        R = [0]*len(height)

        L[0] = height[0]
        for i in range(1, len(height)):
            L[i] = max(height[i], L[i-1])
        last = len(height) - 1
        R[last] = height[last]
        last -= 1
        while last >= 0:
            R[last] = max(height[last], R[last+1])
            last -= 1
        for i in range(0, len(height)):
            water_trapped += min(L[i], R[i]) - height[i]
        return water_trapped
