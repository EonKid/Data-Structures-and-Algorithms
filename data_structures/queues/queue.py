#!/bin/python3
# https://www.coursera.org/learn/data-structures/lecture/EShpq/queues


class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, key):
        node = Node(key)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head is None:
            print("ERROR: queue is empty")
            return
        current_node = self.head
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = self.tail = None
        return current_node

    def traverse(self):
        if self.head is None:
            print("ERROR: queue is empty")
            return
        p = self.head
        while p is not None:
            print(p.key)
            p = p.next


queue = Queue()
print("enqueue:")
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.traverse()

print("deque: ", queue.dequeue().key)
print("deque: ", queue.dequeue().key)
print("deque: ", queue.dequeue().key)
print("is_empty: ", queue.is_empty())
print("taverse: ")
queue.traverse()

