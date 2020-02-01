"""

https://leetcode.com/problems/house-robber/

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""


class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        T = {}
        T[0] = nums[0]
        T[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            T[i] = max(T[i-2] + nums[i], T[i-1])
        return T[len(nums)-1]


sol = Solution()
print(sol.rob([2,7,9,3,1]))

