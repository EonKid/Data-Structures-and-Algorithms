#!/bin/python3
# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        head = prev = node
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next
            prev.next = node
            prev = node

        while l1 is not None:
            node = l1
            prev.next = node
            prev = node
            l1 = l1.next
        while l2 is not None:
            node = l2
            prev.next = node
            prev = node
            l2 = l2.next
        return head.next



