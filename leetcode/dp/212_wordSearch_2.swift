// https://leetcode.com/problems/word-search-ii/


class Solution {

    class Trie{

        class TrieNode{

            var childrens = [TrieNode?]()
            var isLeaf = false
            var item = ""

            init(){
                self.childrens = Array.init(repeating: nil, count : 26)
            }

        }

        var root : TrieNode?
         var baseIndex = Int(Character("a").asciiValue!)

        init(){
            self.root = TrieNode()
        }

        func insert(_ words: [Character]){
               var node = self.root
                for c in words{
                    let index = Int(c.asciiValue!) - baseIndex
                     if node?.childrens[index] == nil{
                            node?.childrens[index] = TrieNode()
                     }
                     node = node?.childrens[index]
                }
                node?.item = String(words)
                node?.isLeaf = true
        }

        func startsWith(_ words: [Character]) -> Bool{
               var node = self.root
                for c in words{
                    let index = Int(c.asciiValue!) - baseIndex
                    if node?.childrens[index] == nil{
                            return false
                     }
                    node = node?.childrens[index]
                }
                return true
        }

        func search(_ words: [Character]) -> Bool {
            var node = self.root
             for c in words{
                 let index = Int(c.asciiValue!) - baseIndex
                 if node?.childrens[index] == nil{
                         return false
                  }
                 node = node?.childrens[index]
            }
            if node?.item == String(words){
                return true
            }
            return false
        }

    }

    var arrResults = Set<String>()

    func dfs(_ board: [[Character]], _ arrVisited: inout [[Bool]], _ row: Int, _ col: Int, _ trie: Trie, _ prefixStr:  String){
           if row < 0 || col < 0 || row >= board.count || col >= board[0].count || arrVisited[row][col]{
                return
           }

           let prefixStr = prefixStr + String(board[row][col])

           if !trie.startsWith(Array(prefixStr)){
                return
            }

            if trie.search(Array(prefixStr)){
                arrResults.insert(String(prefixStr))
            }

            arrVisited[row][col] = true

            dfs(board, &arrVisited, row - 1, col, trie, prefixStr)
            dfs(board, &arrVisited, row + 1, col, trie, prefixStr)
            dfs(board, &arrVisited, row, col - 1, trie, prefixStr)
            dfs(board, &arrVisited, row, col + 1, trie, prefixStr)

            arrVisited[row][col] = false


    }

    func findWords(_ board: [[Character]], _ words: [String]) -> [String] {
           var arrVisited = Array.init(repeating: Array.init(repeating: false, count: board[0].count), count: board.count)
          let trie = Trie()
          for word in words{
                trie.insert(Array(word))
          }

          for row in 0 ..< board.count{
                for col in 0 ..<  board[0].count{
                    let prefixStr = ""
                    dfs(board, &arrVisited, row, col, trie, prefixStr)
                }
        }

        return Array(arrResults)

    }


}