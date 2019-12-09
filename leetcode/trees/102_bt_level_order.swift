//https://leetcode.com/problems/binary-tree-level-order-traversal/

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


    func levelOrder(_ root: TreeNode?) -> [[Int]] {
        if root == nil{
            return []
        }
       var result = [[Int]]()
       var queue = [TreeNode?]()
        queue.append(root)
        while !queue.isEmpty {
            var temp = [Int]()
            var count = queue.count - 1
            while count >= 0 {
                if let node = queue.removeFirst(){
                    temp.append(node.val)
                    count -=  1
                    if let left = node.left{
                        queue.append(left)
                    }
                    if let right = node.right{
                        queue.append(right)
                    }
                }
            }
            result.append(temp)
        }

       return result
    }
}

let sol = Solution()
let root = TreeNode.init(3)
let left = TreeNode.init(9)
let right = TreeNode.init(20)
let right_6 = TreeNode.init(15)
let left_3 = TreeNode.init(7)
root.left = left
root.right = right
right.right = right_6
right.left = left_3
print(sol.levelOrder(root))
