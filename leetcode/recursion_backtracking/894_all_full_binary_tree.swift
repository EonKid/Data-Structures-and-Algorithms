
// https://leetcode.com/problems/all-possible-full-binary-trees/

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

    var dp =  [Int: [TreeNode?]]()

    func helper(_ N: Int)-> [TreeNode?]{
        if let arrData = dp[N]{ return arrData }
        var result = [TreeNode?]()
        if N == 1{
            let node = TreeNode(0)
            return [node]
        }else if N % 2 == 1{
                for x in 0 ..< N{
                    let y = N - 1 - x
                    for left in self.allPossibleFBT(x){
                        for right in self.allPossibleFBT(y){
                            let node = TreeNode(0)
                            node.left = left
                            node.right = right
                            result.append(node)
                        }
                    }
                }
            }

            dp[N] = result

        return dp[N]!
    }

    func allPossibleFBT(_ N: Int) -> [TreeNode?] {
        return helper(N)
    }
}
