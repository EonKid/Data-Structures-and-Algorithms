// https://leetcode.com/problems/symmetric-tree/

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

    func isMirror(_ root: TreeNode?, rootMirror: TreeNode?)-> Bool{
        if root == nil && rootMirror == nil {
            return true
        }
        if root == nil || rootMirror == nil {
            return false
        }

        return (root!.val == rootMirror!.val) && isMirror(root?.left, rootMirror: rootMirror?.right) && isMirror(root?.right, rootMirror: rootMirror?.left)

    }


    func isSymmetric(_ root: TreeNode?) -> Bool {

        return isMirror(root, rootMirror: root)
    }


}

let sol = Solution()
let root = TreeNode.init(1)
let left = TreeNode.init(2)
let right = TreeNode.init(2)
root.left = left
root.right = right



print(sol.isSymmetric(root))
