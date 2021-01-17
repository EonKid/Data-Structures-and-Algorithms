// https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

/*
    3
   / \
  9  20
    /  \
   15   7
*/

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

    func zigzagLevelOrder(_ root: TreeNode?) -> [[Int]] {
        var result = [[Int]]()
        var queue = [TreeNode?]()

        if root == nil {
        	return []
        }

        queue.append(root)

        var level = 0

        while true {

        	var nodeCount = queue.count
        	level += 1

        	if nodeCount == 0 {
        	   break
        	}

        	var levelData = [Int]()

        	while nodeCount > 0 {

        		if let node = queue.removeFirst(){
        		levelData.append(node.val)

        		if let left = node.left {
	    		    queue.append(left)
	    		}

	    		if let right = node.right {
	    		  	queue.append(right)
	    		}

	    		nodeCount -= 1
               }
            }

            if levelData.count > 0 {
               if level % 2 == 0 {
                   result.append(levelData.reversed())
               } else {
            		result.append(levelData)
               }
            }

        }

        return result
    }

}