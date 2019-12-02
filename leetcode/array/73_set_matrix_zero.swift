// Swift
// https://leetcode.com/problems/set-matrix-zeroes/

import Foundation

class Solution {

    func setZeroes(_ matrix: inout [[Int]]) {
        var rows = Array<Int>()
        var columns = Array<Int>()
        for i in 0 ..< matrix.count{
            for j in 0 ..< matrix[i].count{
                if matrix[i][j] == 0{
                    rows.append(i)
                    columns.append(j)
                }
            }
        }


        for row in rows{
            for i in 0 ..< matrix[row].count{
                matrix[row][i] = 0
            }
        }

        for column in columns{
            for i in 0 ..< matrix.count{
                matrix[i][column] = 0
            }
        }
    }

}


let sol = Solution()
var arr = [[0,1]]
print(sol.setZeroes(&arr))



