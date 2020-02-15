"""
Data Structures: Binary Search Tree
https://www.coursera.org/learn/data-structures/lecture/T3oPE/basic-operations

Reference:
https://www.sanfoundry.com/python-program-construct-binary-search-tree-perform-deletion-inorder-traversal/

"""


class Node:

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def find(self, k, R: Node):
        """
        The node in the tree of R with key k
        :param k:
        :type k:
        :param R:
        :type R:
        :return:
        :rtype:
        """
        if R.key == k:
            return R
        elif R.key > k:
            if R.left is not None:
                return self.find(k, R.left)
            else:
                return R
        elif R.key < k:
            if R.right is not None:
                return self.find(k, R.right)
            return R

    def left_descendant(self, N: Node):
        if N.left is None:
            return N
        else:
            return self.left_descendant(N.left)

    def right_ancestor(self, N: Node):
        if N.key < N.parent.key:
            return N.parent
        else:
            return self.right_ancestor(N.parent)

    def next(self, N: Node) -> Node:
        """
        The node in the tree with the next largest key.
        :param N:
        :type N:
        :return:
        :rtype:
        """
        if N.right is not None:
            return self.left_descendant(N.right)
        else:
            return self.right_ancestor(N)

    def range_search(self, x, y, R):
        """
        A list of nodes with key between x and y
        :param x:
        :type x:
        :param y:
        :type y:
        :param R:
        :type R:
        :return:
        :rtype:
        """
        L = []
        N = self.find(k=x, R=R)
        while N.key <= y:
            if N.key >= x:
                L.append(N.key)
            N = self.next(N)
        return L

    def insert(self, k, R):
        """
        Adds node with key k to the tree
        :param k:
        :type k:
        :param R:
        :type R:
        :return:
        :rtype:
        """
        P = self.find(k=k, R=R)
        node = Node(key=k)
        node.parent = P
        if P.left is None:
            P.left = node
        else:
            P.right = node

    def min_value(self, node) -> Node:
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def delete(self,key, root: Node) -> Node:
        """
        Removes node N from the tree
        :param N:
        :type N:
        :return:
        :rtype:
        """
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(key, root.left)
        elif key > root.key:
            root.right = self.delete(key, root.right)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value(root.right)
            root.key = temp.key
            root.right = self.delete(temp.key, root.right)
        return root

    def inorder_traversal(self, node: Node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.key)
        self.inorder_traversal(node.right)


node = Node(key=-10)
bst = BinarySearchTree(node)
bst.insert(-3, bst.root)
bst.insert(0, bst.root)
bst.insert(5, bst.root)
bst.insert(9, bst.root)

# bst.inorder_traversal(bst.root)
# print(bst.range_search(5,12,bst.root))
# search_node = bst.find(13, bst.root)
# print('parent', search_node.parent.key)
# print('search', bst.next(search_node).key)
# bst.delete(13,bst.root)
print("traverse")
bst.inorder_traversal(bst.root)
# print(bst.left_descendant(search_node).key)
# print(bst.right_ancestor(search_node).key)
