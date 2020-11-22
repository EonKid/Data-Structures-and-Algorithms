# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:

  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def in_order(self, root):
      if root == -1:
          return
      self.in_order(self.left[root])
      self.result.append(self.key[root])
      self.in_order(self.right[root])

  def inOrder(self):
    self.result = []
    self.in_order(0)
    return self.result

  def pre_order(self, root):
      if root == -1:
          return
      self.result.append(self.key[root])
      self.pre_order(self.left[root])
      self.pre_order(self.right[root])

  def preOrder(self):
    self.result = []
    self.pre_order(0)
    return self.result

  def post_order(self, root):
      if root == -1:
          return
      self.post_order(self.left[root])
      self.post_order(self.right[root])
      self.result.append(self.key[root])

  def postOrder(self):
    self.result = []
    self.post_order(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
