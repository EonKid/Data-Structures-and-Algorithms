
"""
https://leetcode.com/problems/add-two-numbers/
2. Add Two Numbers
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        prev = head
        carry = 0
        while l1 != None or l2 != None:
            val_1 = 0
            val_2 = 0
            if l1 != None:
                val_1 = l1.val
                l1 = l1.next
            if l2 != None:
                val_2 = l2.val
                l2 = l2.next
            result = carry + val_1 + val_2
            carry = result // 10
            prev.next = ListNode(result % 10)
            prev = prev.next
        if carry != 0:
            prev.next = ListNode(carry)
        return head.next