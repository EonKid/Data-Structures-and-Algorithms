// https://leetcode.com/problems/minimum-window-substring/


class Solution {
    func minWindow(_ s: String, _ t: String) -> String {
         if s.count == 0 || s.count < t.count {
             return ""
         }
         var s = Array(s)
         var tMap = [Character: Int]()
         var t = Array(t)
         for tChar in t {
             if let leftCount = tMap[tChar]{
                 tMap[tChar] = leftCount + 1
             }else{
                 tMap[tChar] = 1
             }
         }

         var windowStart = 0
         var minLen = s.count + 1
         var coverCount = 0
         var minStart = 0

         for windowEnd in stride(from: 0, to: s.count, by: 1){
             if tMap[s[windowEnd]] != nil{
             let leftChar = s[windowEnd]
             if let leftCount = tMap[leftChar]{
                 tMap[leftChar] = leftCount - 1
             }
             if let leftCount = tMap[leftChar]{
                 if leftCount >= 0{
                     coverCount += 1
                 }
             }

             while coverCount == t.count {
                 if windowEnd - windowStart + 1 < minLen{
                     minStart = windowStart
                     minLen = windowEnd - windowStart + 1
                 }
                 let rightChar = s[windowStart]
                 if let rightCount = tMap[rightChar]{
                     tMap[rightChar] = rightCount + 1
                      if rightCount + 1 > 0{
                       coverCount -= 1
                    }
                 }

                 windowStart += 1
              }
          }

         }

         if minLen > s.count {
             return ""
         }
         let result = String(s[minStart...minStart + minLen-1])
         return result

    }
}