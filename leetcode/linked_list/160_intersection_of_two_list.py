"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_a = headA
        p_b = headB
        T = set()

        while p_a is not None:
            T.add(p_a)
            p_a = p_a.next

        while p_b is not None:
            if p_b in T:
                return p_b
            p_b = p_b.next
        return None
