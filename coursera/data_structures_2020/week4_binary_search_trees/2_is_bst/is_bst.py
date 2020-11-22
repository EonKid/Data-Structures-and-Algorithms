#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:

  def __init__(self, key, left, right):
    self.key = key
    self.left = left
    self.right = right

def in_order_traversal(tree):
  nodes = []
  result = []
  stack = []
  current = 0
  for node in tree:
    nodes.append(Node(key=node[0], left= node[1], right= node[2]))

  while stack or current != -1:
    if current != -1:
      root = nodes[current]
      stack.append(root)
      current = root.left
    else:
      root = stack.pop()
      result.append(root.key)
      current = root.right
  return result

def IsBinarySearchTree(tree):
  if len(tree) == 0:
    return True
  nodes = in_order_traversal(tree)
  for i in range(1, len(nodes)):
    if nodes[i] <= nodes[i - 1]:
      return False
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
