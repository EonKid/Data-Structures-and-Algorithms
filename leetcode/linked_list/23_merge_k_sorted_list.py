# Use Python 2 to test the code
# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

# from Queue import PriorityQueue
from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: [ListNode]) -> ListNode:

        head = current_point = ListNode(0)

        p_queue = PriorityQueue()

        for node in lists:
            if node:
                p_queue.put((node.val, node))

        while not p_queue.empty():
            val, node = p_queue.get()
            current_point.next = ListNode(val)
            node = node.next
            current_point = current_point.next
            if node:
                p_queue.put((node.val, node))

        return head.next