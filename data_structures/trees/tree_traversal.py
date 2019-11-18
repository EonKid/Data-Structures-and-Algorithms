"""
Data Structures: DFS In-order traversal
https://www.coursera.org/learn/data-structures/lecture/fr51b/tree-traversal
"""

from data_structures.queues.queue import Queue


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def add_root_node(self, node):
        self.root = node

    def inorder_traversal(self, next):
        """
        Depth-first: In-order traversal
            LDR - left->data->right
        :param next:
        :type next:
        :return:
        :rtype:
        """
        if next is None:
            return
        self.inorder_traversal(next.left)
        print(next.key)
        self.inorder_traversal(next.right)

    def preorder_traversal(self, next):
        """
        Depth-first: Pre-order traversal
             DLR: data->left->right
        :param next:
        :type next:
        :return:
        :rtype:
        """
        if next is None:
            return
        print(next.key)
        self.preorder_traversal(next.left)
        self.preorder_traversal(next.right)

    def postorder_traversal(self, next):
        """
        Depth-first: Post-order traversal
             LRD: left->right->data
        :param next:
        :type next:
        :return:
        :rtype:
        """
        if next is None:
            return
        self.postorder_traversal(next.left)
        self.postorder_traversal(next.right)
        print(next.key)

    def level_traversal(self, next):
        """
        Breadth-first: traversal nodes level by level
        :param next:
        :type next:
        :return:
        :rtype:
        """
        if next is None:
            return
        queue = Queue()
        queue.enqueue(next)
        while not queue.is_empty():
            node = queue.dequeue().key
            print(node.key)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)


def get_binary_tree():
    tree = Tree()
    node_les = Node("Les")
    node_cathy = Node("Cathy")
    node_les.left = node_cathy
    node_alex = Node("Alex")
    node_frank = Node("Frank")
    node_cathy.left = node_alex
    node_cathy.right = node_frank

    node_sam = Node("Sam")
    node_les.right = node_sam
    node_nancy = Node("Nancy")
    node_violet = Node("Violet")
    node_sam.left = node_nancy
    node_sam.right = node_violet
    node_tony = Node("Tony")
    node_wendy = Node("Wendy")
    node_violet.left = node_tony
    node_violet.right = node_wendy
    tree.add_root_node(node_les)
    return tree


tree = get_binary_tree()
print("DFS: In-Order Traversal ")
tree.inorder_traversal(tree.root)
print("DFS: Pre-order traversal")
tree.preorder_traversal(tree.root)
print("DFS: Post-order traversal: ")
tree.postorder_traversal(tree.root)
print("BFS: Level traversal")
tree.level_traversal(tree.root)
