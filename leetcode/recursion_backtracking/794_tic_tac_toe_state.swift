// https://leetcode.com/problems/valid-tic-tac-toe-state/


class Solution {

    func isWinner(_ arrMoves: [String], _ winnerChar: String) -> Bool{
        let arrWinMoves =  [
                            [0, 1,2],[ 3, 4, 5 ], [ 6, 7, 8 ],
                            [0, 4, 8], [2, 4, 6],
                            [0, 3, 6],[1, 4, 7], [2, 5, 8]
                            ]
        for i in 0 ..< arrWinMoves.count{
             if arrMoves[arrWinMoves[i][0]] == winnerChar && arrMoves[arrWinMoves[i][1]] == winnerChar && arrMoves[arrWinMoves[i][2]] == winnerChar{
                return true
             }
         }

         return false
    }

    func validTicTacToe(_ board: [String]) -> Bool {
         var arrMoves = [String]()
         for move in board{
             let data = Array(move)
             for char in data{
                arrMoves.append(String(char))
             }
         }

         var countX = 0
         for char in arrMoves{
             if char == "X"{
                countX += 1
             }
         }

         var countO = 0
         for char in arrMoves{
             if char == "O"{
             countO += 1
             }
         }

         // Base case
         if countX == countO || countX == countO + 1{

               //check if "O" is winner
               if isWinner(arrMoves, "O"){
                   if isWinner(arrMoves, "X"){
                       return false
                   }
                   if countO == countX {
                      return true
                  }
               }

               // check if "X" is valid winner
               if isWinner(arrMoves, "X") && countX != countO + 1{
                  return false
               }

               // check if "O" is not winner
               if !isWinner(arrMoves, "O"){
                    return true
               }
         }

         return false
    }

}

let sol = Solution()
var dataTicTacToe = ["XOX", "O O", "XOX"]
print("Is valid tic-tac-toe: \(sol.validTicTacToe(dataTicTacToe))")