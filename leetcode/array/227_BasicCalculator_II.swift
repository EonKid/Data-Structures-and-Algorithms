// https://leetcode.com/problems/basic-calculator-ii/

class Solution {

    func calculate(_ s: String) -> Int {
         let s = Array(s)
         var operation = Character("+")
         var currentNum = 0
         var lastNumber = 0
         var result = 0

         for i in stride(from: 0, to: s.count, by: 1){
               if s[i].isNumber {
                   currentNum = currentNum * 10 + Int(String(s[i]))!
                 }

               if !s[i].isNumber && s[i] != " " || i == s.count - 1 {
                      if operation == "-" || operation == "+" {
                         result += lastNumber
                         lastNumber = (operation == "+") ? currentNum : -currentNum
                      }

                      if operation == "*" {
                        lastNumber =  (lastNumber * currentNum)
                      }

                     if operation == "/" {
                        lastNumber = (lastNumber / currentNum)
                     }
                     operation = Character(String(s[i]))
                     currentNum = 0
                }

        }
        result += lastNumber
        return result
    }

}

