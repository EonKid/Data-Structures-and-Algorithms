#!bin/python3
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        p = head
        while p is not None:
            next_node = p.next
            p.next = prev
            prev = p
            p = next_node
        head = prev
        return head
