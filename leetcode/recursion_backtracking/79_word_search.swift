//https://leetcode.com/problems/word-search/

 class Solution {

        var arrVisited = [[Bool]]()

        func dfs2(_ board: inout [[Character]], _ i: Int, _ j: Int,_ wordPointer: Int, _ word: [Character])-> Bool{
            let m = board.count
            let n = board[0].count

             if wordPointer == word.count{
                return true
             }

             if i < 0 || j < 0 || i >= m || j >= n || String(board[i][j]) != String(word[wordPointer]){
                      return false
              }


             let temp = board[i][j]
            board[i][j] = "#"
             if     dfs2(&board,i+1, j, wordPointer+1, word)
                 || dfs2(&board, i-1, j, wordPointer+1, word)
                 || dfs2(&board, i, j+1, wordPointer+1, word)
                 || dfs2(&board, i, j-1, wordPointer+1, word){

                return true
             }
             board[i][j] = temp
            return false
        }

        func dfs(_ board: [[Character]], _ i: Int, _ j: Int,_ wordPointer: Int, _ word: [Character]) -> Bool{
            let m = board.count
            let n = board[0].count

            if wordPointer == word.count{
               return true
            }

            if i < 0 || j < 0 || i >= m || j >= n || arrVisited[i][j] || String(board[i][j]) != String(word[wordPointer]){
                     return false
             }


            arrVisited[i][j] = true
            if     dfs(board,i+1, j, wordPointer+1, word)
                || dfs(board, i-1, j, wordPointer+1, word)
                || dfs(board, i, j+1, wordPointer+1, word)
                || dfs(board, i, j-1, wordPointer+1, word){

               return true
            }
            arrVisited[i][j] = false
           return false

        }

        func exist(_ board: [[Character]], _ word: String) -> Bool {
            var board = board
            let m = board.count
            let n = board[0].count
            let arrWord = Array(word)
            //arrVisited = Array.init(repeating: Array.init(repeating: false, count: n), count: m)

               for i in 0 ..< m{
                    for j in 0 ..< n{
                        if String(board[i][j]) == String(arrWord[0]) && dfs2(&board, i,j,0,arrWord){
                                    return true
                             }
                    }
               }


            return false
        }

    }



