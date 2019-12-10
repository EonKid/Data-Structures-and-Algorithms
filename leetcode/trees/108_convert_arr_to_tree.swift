// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import Foundation

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}
 
class Solution {
    
    func convertToBST(_ nums: [Int],_ low: Int,_ high: Int)-> TreeNode?{
        if low > high{
            return nil
        }
        let middle = (low+high)/2
        let root = TreeNode.init(nums[middle])
        root.left = convertToBST(nums, low, middle-1)
        root.right = convertToBST(nums, middle+1, high)
        return root
    }
    
    func sortedArrayToBST(_ nums: [Int]) -> TreeNode? {
        if nums.count == 0{
            return nil
        }
        return convertToBST(nums, 0, nums.count - 1)
    }
}

let sol = Solution()
let nums = [-10,-3,0,5,9]
let root = sol.sortedArrayToBST(nums)
print(root?.val)


