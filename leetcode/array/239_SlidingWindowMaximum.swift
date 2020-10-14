// https://leetcode.com/problems/sliding-window-maximum/

class Solution {

    func maxSlidingWindow(_ nums: [Int], _ k: Int) -> [Int] {
         let n = nums.count
         var result = Array.init(repeating: 0, count: n - k + 1 )
         var windowStart = 0
         var deque = [Int]()


         for windowEnd in stride(from: 0, to: n, by: 1){

            //remove number out of range
            while !deque.isEmpty && deque.first! < windowEnd - k + 1 {
                deque.removeFirst()
            }

            // remove smaller numbers in k range as they are useless
            while !deque.isEmpty && nums[deque.last!] < nums[windowEnd]{
                deque.removeLast()
            }

            // deque contains index... result contains content
            deque.append(windowEnd)
            if windowEnd >= k - 1 {
                result[windowStart] = nums[deque.first!]
                windowStart += 1
            }

         }
         return result
    }

}