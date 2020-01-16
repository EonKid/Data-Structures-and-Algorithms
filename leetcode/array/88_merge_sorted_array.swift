
// https://leetcode.com/problems/merge-sorted-array/

import Foundation

class Solution {
    func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {

        var i = 0
        var j = 0
        var k = 0
        var arrResult = Array.init(repeating: 0, count: m+n)

        while i < m && j < n {
            if nums1[i] <= nums2[j] {
                arrResult[k] = nums1[i]
                i += 1
            }else{
                arrResult[k] = nums2[j]
                j += 1
            }
            k += 1

        }

        while i < m{
            arrResult[k] = nums1[i]
            i += 1
            k += 1
        }

        while j < n{
            arrResult[k] = nums2[j]
            j += 1
            k += 1
        }
        nums1 = arrResult

    }
}

var nums1 = [1,2,3,0,0,0]
var m = 3
var nums2 = [2,5,6]
var n = 3

let sol = Solution()
sol.merge(&nums1, m, nums2, n)


