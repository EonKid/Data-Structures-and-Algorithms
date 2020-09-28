// https://leetcode.com/problems/4sum-ii/

//Time complexity - O(n^2)
// Space complexity - O(n^2)

class Solution {
    func fourSumCount(_ A: [Int], _ B: [Int], _ C: [Int], _ D: [Int]) -> Int {
         var memo = [Int: Int]()
			 var count = 0

			// a + b

			for i in stride(from:0, to: A.count, by: 1){
					for j in stride(from: 0, to: B.count, by: 1){
							var sum = A[i] + B[j]
							if memo[sum] != nil {
								memo[sum]! += 1
							}else{
								memo[sum] = 1
							}
					}
			}


			// c + d
				for i in stride(from: 0, to: C.count, by: 1){
						for j in stride(from: 0, to: D.count, by: 1){
							 let sum = -1 * ( C[i] + D[j])
							 if memo[sum] != nil{
									count += memo[sum]!
							 }
						}
				}



			 return count
    }
}

