// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

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

    func helper(_ preorder: [Int], _ id: inout  Int,_ min: Int, _ limit: Int) -> TreeNode?{

        if id >= preorder.count {
            return nil
        }

        var rootValue = preorder[id]

        if  rootValue < min || rootValue > limit {
            return nil
        }

        var root =  TreeNode(rootValue)
        id += 1
        root.left = helper(preorder, &id, min, rootValue - 1)
        root.right = helper(preorder, &id, rootValue + 1, limit)
        return root

    }

    func bstFromPreorder(_ preorder: [Int]) -> TreeNode? {
        var id = 0
        return helper(preorder, &id, Int.min,Int.max)
    }
}