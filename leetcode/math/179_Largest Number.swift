// https://leetcode.com/problems/largest-number/

/*

nums = [3,30,34,5,9]

*/

class Solution {


    func largestNumber(_ nums: [Int]) -> String {
         let largestNum = nums.map{ String($0) }.sorted{ $0 + $1 > $1 + $0 }
         if largestNum[0] == "0"{
             return "0"
         }
         return largestNum.joined()
    }
    
}