#!/bin/python3
"""
Topic: Doubly-Linked Lists
https://www.coursera.org/learn/data-structures/lecture/jpGKD/doubly-linked-lists

"""


class Node:

    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def push_top(self, key):
        node = Node(key)
        node.key = key
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def traverse(self):
        if self.head is None:
            print("Error: Doubly linked list is empty")
            return
        else:
            p = self.head
            while p is not None:
                print(p.key)
                p = p.next

    def top_front(self):
        if self.head is not None:
            return self.head

    def add_after(self, node, key):
        node2 = Node(key)
        node2.next = node.next
        node2.prev = node
        node.next = node2
        if node2.next is not None:
            node2.next.prev = node2
        if self.tail is node:
            self.tail = node2

    def add_before(self, node, key):
        node2 = Node(key)
        node2.next = node
        node2.prev = node.prev
        node.prev = node2
        if node2.prev is not None:
            node2.prev.next = node2
        if self.head is node:
            self.head = node2

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.push_top("1")
doubly_linked_list.push_top("2")
doubly_linked_list.push_top("3")
doubly_linked_list.push_top("4")
doubly_linked_list.traverse()
print("top front: ", doubly_linked_list.top_front().key)
print("add after: ")
doubly_linked_list.add_after(doubly_linked_list.top_front(), "5")
doubly_linked_list.traverse()
print("add before:")
doubly_linked_list.add_before(doubly_linked_list.top_front(), "6")
doubly_linked_list.traverse()