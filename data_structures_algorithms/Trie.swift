// https://www.programcreek.com/2014/05/leetcode-implement-trie-prefix-tree-java/
// https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie {

    var root: TrieNode?

    class TrieNode{

        var childrens = [TrieNode?]()
        var isEnd = false
        var item : String?

        init(){
            self.childrens = Array.init(repeating: nil, count: 26)
        }

    }

    /** Initialize your data structure here. */
    init() {
        self.root = TrieNode()
    }

    /** Inserts a word into the trie. */
    func insert(_ word: String) {
        var currentNode = self.root
        let arrData = Array(word)
        let baseIndex = Int(Character("a").asciiValue!)
        for i in 0 ..< arrData.count{
            let currentChar = arrData[i]
            let currentIndex = Int(currentChar.asciiValue!)
            let index = currentIndex - baseIndex
            if currentNode?.childrens[index] == nil{
                currentNode?.childrens[index] = TrieNode()
            }
            currentNode = currentNode?.childrens[index]
        }
        currentNode?.isEnd = true
        currentNode?.item = word
    }

    /** Returns if the word is in the trie. */
    func search(_ word: String) -> Bool {
          var currentNode = self.root
        let arrData = Array(word)
           for i in 0 ..< arrData.count{
            let currentChar = arrData[i]
            let currentIndex = Int(currentChar.asciiValue!)
            let baseIndex = Int(Character("a").asciiValue!)
            let index = currentIndex - baseIndex
            if currentNode?.childrens[index] == nil{
               return false
            }
            currentNode = currentNode?.childrens[index]
           }

        if currentNode?.item == word{
                return true
        }else{
                return false
        }
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    func startsWith(_ prefix: String) -> Bool {
           var currentNode = self.root
        let arrData = Array(prefix)
           for i in 0 ..< arrData.count{
            let currentChar = arrData[i]
            let currentIndex = Int(currentChar.asciiValue!)
            let baseIndex = Int(Character("a").asciiValue!)
            let index = currentIndex - baseIndex
            if currentNode?.childrens[index] == nil{
               return false
            }
            currentNode = currentNode?.childrens[index]
           }
           return true
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * */
let dataChars = "banana"
  let obj = Trie()
 obj.insert(dataChars)
 let ret_2: Bool = obj.search(dataChars)
 let ret_3: Bool = obj.startsWith("b")