#!/bin/python3
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = p = head
        size = 1
        while current.next:
            size += 1
            current = current.next
            if size > n+1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head




