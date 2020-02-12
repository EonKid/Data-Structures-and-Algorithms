/*

94. Binary Tree Inorder Traversal


https://leetcode.com/problems/binary-tree-inorder-traversal/

*/


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
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        var arrResult = [Int]()
        var stack = [TreeNode]()
        var currentNode = root
        while currentNode != nil || !stack.isEmpty{
            if currentNode != nil{
                stack.append(currentNode!)
                currentNode = currentNode?.left
            }else{
                currentNode = stack.popLast()
                arrResult.append(currentNode!.val)
                currentNode = currentNode?.right
            }
            
        }
        return arrResult
    }
}