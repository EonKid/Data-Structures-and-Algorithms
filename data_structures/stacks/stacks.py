"""
Stacks
LIFO - Last in First Out
https://www.coursera.org/learn/data-structures/lecture/UdKzQ/stacks

"""


class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None: return True
        else: return False

    def top_stack(self):
        return self.head

    def push_stack(self, key):
        node = Node(key)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            self.head = node
            node.next = current_node

    def pop_stack(self):
        if self.head is None:
            print("Error: stack empty")
            return
        head_node = self.head
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = None
        return head_node

    def traverse(self):
        if self.head is Node:
            print("Error: Stack is empty")
        next = self.head
        while next is not None:
            print(next.key)
            next = next.next


stack = Stack()
stack.push_stack("a")
stack.push_stack("b")
stack.push_stack("c")
stack.push_stack("d")
print("Stack traverse: ")
stack.traverse()
print("stack top: ", stack.top_stack().key)
print("stack pop: ", stack.pop_stack().key)
print("stack pop: ", stack.pop_stack().key)
print("stack pop: ", stack.pop_stack().key)
print("stack pop: ", stack.pop_stack().key)
print("stack pop: ", stack.pop_stack())

print("stack traverse: ")
stack.traverse()
