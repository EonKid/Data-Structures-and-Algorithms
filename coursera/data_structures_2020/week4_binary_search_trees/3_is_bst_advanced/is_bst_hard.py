#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:

  def __init__(self, key, left, right):
    self.key = key
    self.left = left
    self.right = right

def IsBinarySearchTree(tree):
  nodes = []
  for node in tree:
    nodes.append(Node(key=node[0], left= node[1], right= node[2]))
  stack = [(float('-inf'), nodes[0], float('inf'))]
  while stack:
    min_val, root, max_val = stack.pop()
    if root.key < min_val or root.key >= max_val:
      return False
    if root.left != -1:
      stack.append((min_val, nodes[root.left], root.key))
    if root.right != -1:
      stack.append((root.key, nodes[root.right], max_val))
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if nodes == 0 or IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
