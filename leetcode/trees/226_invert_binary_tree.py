from queue import Queue

"""

https://leetcode.com/problems/invert-binary-tree/

Input

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return root
        nodes_queue = Queue()
        nodes_queue.put(root)

        while not nodes_queue.empty():
            current_node = nodes_queue.get()
            temp_node = current_node.left
            current_node.left = current_node.right
            current_node.right = temp_node

            if current_node.left is not None:
               nodes_queue.put(current_node.left)
            if current_node.right is not None:
               nodes_queue.put(current_node.right)

        return root