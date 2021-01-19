// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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

    var dp = [Int: Int]()

    func helper(_ preStart: Int,_ inStart: Int,_ inEnd: Int,_ preorder: [Int], _ inorder: [Int]) -> TreeNode?{
        if preStart > preorder.count - 1 || inStart > inEnd{
            return nil
        }

        var inIndex = 0
        let rootValue = preorder[preStart]
        inIndex = dp[rootValue]!
        var root = TreeNode(rootValue)
        root.left = helper(preStart + 1, inStart, inIndex - 1, preorder, inorder)
        root.right = helper(preStart + inIndex - inStart + 1, inIndex + 1, inEnd, preorder, inorder)
        return root
    }

    func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
        for i in 0 ..< inorder.count{
            dp[inorder[i]] = i
        }
        return helper(0, 0, inorder.count - 1, preorder, inorder)
    }
}