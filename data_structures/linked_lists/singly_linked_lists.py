#!/bin/python3


class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Front cases:

    def push_front(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def pop_front(self):
        if self.head is None:
            print("Linked List is empty")
        front_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = self.head
        return front_node

    def top_front(self):
        if self.head is None:
            print("Linked List is empty")
        return self.head

    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            next = self.head
            while next is not None:
                print(next.key)
                next = next.next


linked_list = LinkedList()
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


