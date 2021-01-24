// https://leetcode.com/problems/inorder-successor-in-bst/


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


   func inorderSuccessor(_ root: TreeNode?, _ p: TreeNode) -> TreeNode?{
        if root == nil {
            return nil
        }
        var current = root
        var res : TreeNode? = nil

        while current != nil {
            if current!.val > p.val {
             // go to left
             res = current
             current = current?.left
           }else{
             // go to right
             current = current?.right
           }
        }

        return res
   }

}

let root = TreeNode(2)
let left = TreeNode(1)
let right = TreeNode(3)
root.left = left
root.right = right
let sol = Solution()
print("Inorder successor in BST: \(sol.inorderSuccessor(root, left)?.val)")