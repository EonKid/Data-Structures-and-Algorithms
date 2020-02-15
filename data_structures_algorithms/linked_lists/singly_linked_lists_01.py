#!/bin/python3
"""
Data Structures by University of California San Diego & National Research University Higher School of Economics
Topic: Singly-Linked Lists
https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists

"""


class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Front operation:

    def push_front(self, key):
        # Time complexity : O(1)
        node = Node(key)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def pop_front(self):
        # Time complexity: O(1)
        if self.head is None:
            print("Error: Linked List is empty")
        front_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = self.head
        return front_node

    def top_front(self):
        # Time complexity: O(1)
        if self.head is None:
            print("Error: Linked List is empty")
        return self.head

    def traverse(self):
        if self.head is None:
            print("Error: Linked List is empty")
            return
        else:
            next = self.head
            while next is not None:
                print(next.key)
                next = next.next

    # Back opertations:

    def push_back(self, key):
        # Time complexity: O(1)
        node = Node(key)
        node.key = key
        node.next = None
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node

    def pop_back(self):
        # Time complexity: O(n)
        if self.head is None:
            print("Error: Linked List is empty")
        if self.head == self.tail:
            current_node = self.head
            self.head = self.tail = None
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
            current_node = self.tail
            p.next = None
            self.tail = p
        return current_node

    def add_after(self, node, key):
        node2 = Node(key)
        node2.next = node.next
        node.next = node2
        if self.tail == node:
            self.tail = node2

linked_list = SinglyLinkedList()

# Front operations
print("Push item: ")
linked_list.push_front("1")
linked_list.push_front("2")
linked_list.push_front("3")
print("Traverse: ")
linked_list.traverse()
print("Pop item: ", linked_list.pop_front().key)
print("Traverse: ")
linked_list.traverse()
print("Top front: ", linked_list.top_front().key)

# Back operations
print("Push back:")
linked_list.push_back("4")
linked_list.push_back("5")
print("Taverse: ")
linked_list.traverse()
print("Pop back")
print("Poped item: ", linked_list.pop_back().key)
linked_list.traverse()
print("Add after: ")
linked_list.add_after(linked_list.top_front(), key="6")
linked_list.traverse()