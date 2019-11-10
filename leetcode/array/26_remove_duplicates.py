#!/bin/python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        slow_pointer = 0
        for fast_pointer in range(1, len(nums)):
            if nums[fast_pointer] != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]
        return slow_pointer+1


sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
