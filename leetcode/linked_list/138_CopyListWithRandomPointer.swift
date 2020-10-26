// https://leetcode.com/problems/copy-list-with-random-pointer/

/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var next: Node?
 *     public var random: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *    	   self.random = nil
 *     }
 * }
 */

class Solution {

    func copyRandomList(_ head: Node?) -> Node? {
        return sol2(head)
    }

    func sol2(_ head: Node?) -> Node? {
        // Time Complexity : O(n)
        // Space complexity : O(1)
        if head == nil{
            return head
        }
        var iterNode = head

        // A -> A' -> B -> B'
        while iterNode != nil {
            var next = iterNode?.next
            var node = Node(iterNode!.val)
            node.next = next
            iterNode?.next = node
            iterNode = next
        }

        // link random of R' ....Rn
        iterNode = head
        while iterNode != nil{
            if iterNode?.random != nil{
                iterNode?.next?.random = iterNode?.random?.next
            }
            iterNode = iterNode?.next?.next
        }

        // A -> A' -> B -> B' -> C -> C'
        // Copy new list A' -> B' -> C'
        // Get back original list A -> B -> C
        iterNode = head
        var copyHead = head?.next
        while iterNode != nil{
            var copy = iterNode?.next
            var next = iterNode?.next?.next
            iterNode?.next = next
            if next != nil{
                copy?.next = next?.next
            }
            iterNode = next
        }

        return copyHead
    }


    func sol1(_ head: Node?) -> Node? {
        // Time complexity: O(n)
        // Space complexity: O(n)

        if head == nil{
            return nil
        }

        var map = [Node:Node]()
        var resultNode : Node? = Node(0)
        var currentNode : Node? = resultNode

        var iterNode = head
        while iterNode != nil{
            currentNode?.next = Node(iterNode!.val)
            map[iterNode!] = currentNode!.next
            iterNode = iterNode?.next
            currentNode = currentNode?.next
        }

        iterNode = head
        currentNode = resultNode?.next
        while currentNode != nil{
            if let node = iterNode{
                if let random = node.random{
                     currentNode!.random = map[random]

                }
            }
                    currentNode = currentNode?.next
                     iterNode = iterNode?.next
        }

        return resultNode?.next
    }

}