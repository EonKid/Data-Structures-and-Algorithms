// https://leetcode.com/problems/validate-binary-search-tree/
 // Definition for a binary tree node.
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

    func checkValidity(_ root: TreeNode?, minValue: Int, maxValue: Int) -> Bool {
        if root == nil {
            return true
        }
        if root!.val <= minValue || root!.val >= maxValue{
            return false
        }
        return checkValidity(root?.left, minValue: minValue, maxValue: root!.val) && checkValidity(root?.right, minValue: root!.val, maxValue: maxValue)
    }

    func isValidBST(_ root: TreeNode?) -> Bool {
        return checkValidity(root, minValue: Int.min, maxValue: Int.max)
    }

}

let sol = Solution()
let root = TreeNode.init(1)
let left = TreeNode.init(1)
//let right = TreeNode.init(4)
//let right_6 = TreeNode.init(6)
//let left_3 = TreeNode.init(3)
root.right = left
//root.left = right
//right.right = right_6
//right.left = left_3
print(sol.isValidBST(root))