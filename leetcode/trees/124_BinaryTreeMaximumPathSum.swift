// https://leetcode.com/problems/binary-tree-maximum-path-sum/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {

    func dfs(_ root: TreeNode?, _  result: inout Int) -> Int{
        guard let root = root else{
            return 0
        }
        let left = dfs(root.left, &result)
        let right = dfs(root.right, &result)

        let singlePathSum = max(max(left, right) + root.val, root.val)
        let twoPathSum = max(left + right + root.val, singlePathSum)
        result = max(twoPathSum, result)
        return singlePathSum
    }

    func maxPathSum(_ root: TreeNode?) -> Int {
        var result = Int.min
        dfs(root, &result)
        return result

    }
}