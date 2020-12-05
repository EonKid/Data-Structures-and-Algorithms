// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class Solution {
    func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode?, _ q: TreeNode?) -> TreeNode? {
        if root === nil || root === p || root === q{
            return root
        }

        let left = lowestCommonAncestor(root?.left, p, q)
        let right = lowestCommonAncestor(root?.right, p, q)

        if left != nil && right != nil{
            return root
        }

        return left != nil ? left : right

    }
}