// https://leetcode.com/problems/permutations/

class Solution {

    func permute(_ nums: [Int]) -> [[Int]] {
        var arrNums = nums
        var result = [[Int]]()
        self.helper(&arrNums, 0, nums.count, &result)
        return result
    }

    func swap(_ nums: inout [Int], _ start: Int, _ end: Int){
         let temp = nums[start]
         nums[start] = nums[end]
         nums[end] = temp
    }

    func helper(_ arrNums: inout [Int],_ startIndex: Int,_ endIndex: Int,_ result: inout [[Int]]){
         if startIndex == endIndex{
            result.append(arrNums)
            return
         }
        for i in startIndex ..< endIndex{
            swap(&arrNums, startIndex, i)
            helper(&arrNums,startIndex+1, endIndex, &result)
            swap(&arrNums, startIndex, i)
        }
    }

}

let sol = Solution()
print(sol.permute([1, 2, 3]))

