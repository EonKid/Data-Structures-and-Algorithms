//https://leetcode.com/problems/n-queens/


    class Solution {

        var arrResult = [[String]]()

        func solveNQueens(_ n: Int) -> [[String]] {
            if n == 0{ return [[]] }
            let arrChars = Array.init(repeating: ".", count: n)
            var board = Array.init(repeating:arrChars, count: n)
            backtrack(&board, 0)
            return arrResult
        }


        func backtrack(_ board: inout [[String]],  _ col: Int){
            let n = board.count
             if col >= n{
                var arrData = [String]()
                for data in board{
                    var resultChars = ""
                    for characters in data{
                        resultChars += characters
                    }
                    arrData.append(resultChars)
                }
                arrResult.append(arrData)
                return
             }

            for i in 0 ..< n{
                 if isSafe(board, i, col){
                        board[i][col] = "Q"
                        backtrack(&board, col+1)
                        board[i][col] = "."
                 }
            }
            return
        }

        func isSafe(_ board:  [[String]], _ row: Int, _ col: Int) -> Bool{
            let n = board.count
            //check rows
            for i in 0 ..< n{
                if board[row][i] == "Q"{
                    return false
                }
            }


            // check upper left
            var i = row
            var j = col
            while i < n && j >= 0 {
                if board[i][j] == "Q"{
                    return false
                }
                i += 1
                j -= 1
            }

            // check upper right
            var k = row
            var l = col
            while k < n && l >= 0 && k >= 0{
                if board[k][l] == "Q"{
                    return false
                }
                k -= 1
                l -= 1
            }

            return true
        }

    }

