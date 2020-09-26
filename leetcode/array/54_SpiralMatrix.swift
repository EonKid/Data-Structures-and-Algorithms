// https://leetcode.com/problems/spiral-matrix/
// Time complexity - O(n) , Space = O(1)



class Solution {

    func spiralOrder(_ matrix: [[Int]]) -> [Int] {

			 if matrix.count == 0{
					return []
			 }

			 var result = [Int]()
			 var rowBegin = 0
			 var rowEnd = matrix.count - 1
			 var colBegin = 0
			 var colEnd = matrix[0].count - 1

			 while rowBegin <= rowEnd && colBegin <= colEnd{

						// traverse right
						for j in stride(from:colBegin, to: colEnd + 1, by: 1){
								result.append(matrix[rowBegin][j])
						}
						rowBegin += 1

						// traverse down
						for i in stride(from:rowBegin, to: rowEnd + 1, by: 1){
								result.append(matrix[i][colEnd])
						}
						colEnd -= 1

						if rowBegin <= rowEnd{
						//traverse left
						 for j in stride(from: colEnd, to: colBegin - 1, by: -1){
							  result.append(matrix[rowEnd][j])
						 }
						}
						rowEnd -= 1

						// traverse up
						if colBegin <= colEnd{
							for i in stride(from: rowEnd, to: rowBegin - 1, by: -1){
									result.append(matrix[i][colBegin])
							}
						}
						colBegin += 1

			 }

			 return result

    }

}
