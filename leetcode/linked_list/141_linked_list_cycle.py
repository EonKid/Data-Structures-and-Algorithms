#!/bin/python3
# https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        visited.add(head)
        while head:
            head = head.next
            if head in visited:
                return True
            visited.add(head)
        return False




