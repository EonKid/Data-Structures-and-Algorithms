// https://leetcode.com/problems/sort-list/
// Time complexity : n log(n)
// Space complexity : log(n)
class Solution {

    func sortList(_ head: ListNode?) -> ListNode? {
               if head == nil {
                    return head
               }

                if head?.next == nil {
                    return head
                }

                var leftNode = head
                var rightNode = findMidWithSplit(head)
                leftNode = sortList(head)
                rightNode = sortList(rightNode)
                return mergeList(leftNode, rightNode)

    }

      func findMidWithSplit(_ head: ListNode?) -> ListNode? {
              var slowNode : ListNode?
              var head = head
              while head != nil && head?.next != nil {
                slowNode = (slowNode == nil) ? head : slowNode?.next
                head = head?.next?.next
              }
              let mainNode = slowNode?.next
              slowNode?.next = nil
              return mainNode
        }

        func mergeList(_ leftNode: ListNode?, _ rightNode: ListNode?) -> ListNode? {
                var leftNode = leftNode
                var rightNode = rightNode
                let mainNode : ListNode? = ListNode(0)
                var pointNode  = mainNode
                while leftNode != nil && rightNode != nil {
                    if let leftVal = leftNode?.val, let rightVal = rightNode?.val{
                        if leftVal < rightVal{
                                 pointNode?.next = leftNode
                                 leftNode = leftNode?.next
                                 pointNode = pointNode?.next
                         }else{
                                 pointNode?.next = rightNode
                                 rightNode = rightNode?.next
                                 pointNode = pointNode?.next
                        }
                    }

                }

            pointNode?.next = (leftNode != nil) ? leftNode : rightNode
            return mainNode?.next

        }

}