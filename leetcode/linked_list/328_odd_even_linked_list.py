"""

https://leetcode.com/problems/odd-even-linked-list/

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: return head
        odd_node = head
        even_node = head.next
        even_head = head.next
        while even_node != None and even_node.next != None:
            odd_node.next = even_node.next
            odd_node = odd_node.next
            even_node.next = odd_node.next
            even_node = even_node.next
        odd_node.next = even_head
        return head
