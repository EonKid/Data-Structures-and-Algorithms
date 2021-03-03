
class Node {

	var isWord = false
	var childNodes = [Node?]()

	init(){
		childNodes = Array.init(repeating: nil, count: 26)
	}

}



class Trie {

     var root = Node()
    var baseIndex = Int(Character(String("a")).asciiValue!)

    /** Initialize your data structure here. */
    init() {

    }

    /** Inserts a word into the trie. */
    func insert(_ word: String) {
	    var currentNode = root
	    var words = Array(word)
	    for char in words {
		  let index = Int(Character(String(char)).asciiValue!) - baseIndex
		  if currentNode.childNodes[index] === nil{
			currentNode.childNodes[index] = Node()
		  }
		  currentNode = currentNode.childNodes[index]!
	    }
	    currentNode.isWord = true

    }

    /** Returns if the word is in the trie. */
    func search(_ word: String) -> Bool {
        var currentNode = root
	   var words = Array(word)
	   for char in words {
		let index = Int(Character(String(char)).asciiValue!) - baseIndex
		if currentNode.childNodes[index] === nil{
			return false
		}
		currentNode = currentNode.childNodes[index]!
	   }
	  return currentNode.isWord
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    func startsWith(_ prefix: String) -> Bool {
        var currentNode = root
	   var words = Array(prefix)
	   for char in words{
		let index = Int(Character(String(char)).asciiValue!) - baseIndex
		if currentNode.childNodes[index] === nil{
			return false
		}
		currentNode = currentNode.childNodes[index]!
	   }

	   return true

    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie()
 * obj.insert(word)
 * let ret_2: Bool = obj.search(word)
 * let ret_3: Bool = obj.startsWith(prefix)
 */