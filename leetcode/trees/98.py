# https://leetcode.com/problems/validate-binary-search-tree/
import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def validate_bst(self,node, min_val, max_val):
        if node is None:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return self.validate_bst(node.left,min_val, node.val) and self.validate_bst(node.right,node.val, max_val)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate_bst(root, float('-inf'), float('inf'))

