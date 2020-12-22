// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution {

    func findIndex(_ curNum: Int, _ sorted: inout [Int]) -> Int{
        if sorted.count == 0{
            return 0
        }
        var start = 0
        var end = sorted.count - 1
        if sorted[start] >= curNum{
            return start
        }
        if sorted[end] < curNum{
            return end + 1
        }
        while start < end{
            let mid = start + (end - start) / 2
            if sorted[mid] < curNum{
                start = mid + 1
            }else{
                end = mid
            }
        }

        if sorted[start] >= curNum{
            return start
        }
        return end
    }

    func countSmaller(_ nums: [Int]) -> [Int] {
        // Time complexity: n*log(n) + n*n
        var sorted = [Int]()
        let N = nums.count
        var result = Array.init(repeating: 0, count: N)
        for i in stride(from: N - 1, to:-1, by: -1 ){
            let curNum = nums[i]
            let index = findIndex(curNum, &sorted)
            result[i] = index
            sorted.insert(curNum, at: index)
        }

        return result

    }
}