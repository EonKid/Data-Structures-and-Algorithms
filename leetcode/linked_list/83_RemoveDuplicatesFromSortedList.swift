// https://leetcode.com/problems/remove-duplicates-from-sorted-list/ 
 // Definition for singly-linked list.
  public class ListNode {
     public var val: Int
    public var next: ListNode?
     public init(_ val: Int) {
        self.val = val
        self.next = nil
     }
  }
 
class Solution {
    func deleteDuplicates(_ head: ListNode?) -> ListNode? {
        var currentNode = head
        while currentNode != nil && currentNode?.next != nil{
        	 if currentNode!.val == currentNode!.next.val{
        	    currentNode!.next = currentNode.next.next
        	 }else{
        	      currentNode = currentNode!.next
        	 }

        }
        return head
    }
}
