#!/bin/python3
# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        p = head
        while p is not None:
            nodes.append(p.val)
            p = p.next
        return nodes == nodes[::-1]



