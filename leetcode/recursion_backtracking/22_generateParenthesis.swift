// https://leetcode.com/problems/generate-parentheses/


class Solution {

    var arrResult = [String]()
    var dictData = [String: Bool]()

    func isValid(_ str: String) -> Bool{
        var balance = 0
        let arrChars = Array(str)
        for currentChar in arrChars{
            let current = String(currentChar)
            if current == "("{
                balance += 1
            }else{
                balance -= 1
            }
            if balance < 0{
                return false
            }
        }
        return balance == 0
    }

    func backtrack(_ combination: String, _ restString: String){
            if restString.count == 0{
                if isValid(combination) {
                    if dictData[combination + restString] == nil{
                    dictData[combination + restString] = true
                    arrResult.append(combination)
                    }
                }
            }else{
                    for i in 0 ..< restString.count{
                        let startIndex = restString.index(restString.startIndex, offsetBy: i)
                        let nextFirstIndex = restString.index(restString.startIndex, offsetBy: i+1)
                        let currentString = String(restString[startIndex])
                        let nextString = String(restString[nextFirstIndex...])
                        let firstHalf = String(restString.prefix(upTo: startIndex))
                        let next = firstHalf + nextString
                        backtrack(combination + currentString, next)
                    }
            }
    }

    func anotherBacktrack(_ strP: inout String, _ left: Int, _ right: Int, _ N: Int){
            if strP.count == (2*N){
                arrResult.append(strP)
                return
            }
            if left < N{
                var str = strP + "("
                anotherBacktrack(&str, left+1, right, N)
            }
            if right < left{
                var str = strP + ")"
                anotherBacktrack(&str, left, right+1, N)
            }
    }

    func generateParenthesis(_ n: Int) -> [String] {

        /*
         var pairs = "()"
         for _ in 1 ..< n{
            pairs += "()"
         }
         print(pairs)
         backtrack("", pairs)
        */
        var str = ""
        anotherBacktrack(&str,0,0, n)
         return arrResult
    }

}

