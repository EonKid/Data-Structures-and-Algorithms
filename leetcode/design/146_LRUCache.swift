
class LRUCache {

    var list : DoublyLinkedList
    var map : [Int : Node]
    var capacity : Int

    init(_ capacity: Int) {
        self.capacity = capacity
        self.list = DoublyLinkedList()
        self.map = [Int: Node]()
    }

    func get(_ key: Int) -> Int {
        var node = map[key]
        if node == nil{
            return -1
        }
        self.list.moveToHead(&node)
        return node!.val
    }

    func put(_ key: Int, _ value: Int) {
        var node = map[key]
        if node != nil {
            node?.val = value
            self.list.moveToHead(&node)
        }else{
            var newNode: Node? = Node(key, value)
            if self.capacity == self.map.count {
                let tail = self.list.getTail()
                self.list.removeTail()
                self.map.removeValue(forKey: tail!.key)
            }
            self.list.addToHead(&newNode)
            self.map[key] = newNode
        }
    }

}

class DoublyLinkedList {

    var head : Node?
    var tail : Node?

    init(){
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head?.next = tail
        self.tail?.prev = self.head
    }

    func moveToHead(_ node: inout Node?){
        node?.prev?.next = node?.next
        node?.next?.prev = node?.prev
        addToHead(&node)
    }

    func addToHead(_ node: inout Node?){
        let tempNode = self.head?.next
        head?.next = node
        node?.next = tempNode
        node?.prev = self.head
        tempNode?.prev = node
    }

    func getTail() -> Node? {
        return self.tail?.prev
    }

    func removeTail(){
        let tailNode = self.tail?.prev?.prev
        tailNode?.next = self.tail
        self.tail?.prev = tailNode

    }

}

class Node {

    var key: Int
    var val : Int
    var next : Node?
    var prev : Node?

    init(_ key: Int,_ val: Int) {
        self.key = key
        self.val = val
    }

}