#!/bin/python3
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        L = []
        T = {}

        for num in nums1:
            if num not in T:
                count = 1
                T[num] = count
            else:
                count = T[num]
                T[num] = count + 1

        for num in nums2:
            if num in T:
                val = T[num]
                if val is not None and T[num] > 0:
                    T[num] = T[num] - 1
                    L.append(num)
            else:
                T[num] = None

        return L


sol = Solution()
n1 = [84,5,30,84,67,78,73,38,93,92,15,43,38,81,68,65,62,21,16,38,95,68,60,35,43,95,67]
n2 = [82,60,70,10,94,6,44,51,1,3,97,84,3,87,91,55,81,90,45,22,18,58,62,96,27,24,16,63,30,60,29,93,27,56,79,4,69,9,21,23,7,49,62,89,22,64,85,75,55,49,57,17,84,49,8,13,94,40,75,50,93,46,36,94,50,0,3,65,49,82,45,11,53,63,27,71,45,37,45,19,21,57,66,99,94,92,44,35,84,78,80,88]
print(sol.intersect(n1, n2))