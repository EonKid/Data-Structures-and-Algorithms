/*
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
*/

class Solution1 {

     let numberPadDict = [
          "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
     ]

    func letterCombinations(_ digits: String) -> [String] {
        var result = [String]()
        func backtrack(_ combination: String, next: String){
            if next.count == 0{
                result.append(combination)
            }else{
                if let letters = numberPadDict[String(next[0])]{
                    print(letters)
                    for letter in letters{
                        let startIndex = next.index(next.startIndex, offsetBy: 1)
                        let restString = String(next[startIndex...])
                        backtrack(combination + String(letter), next: restString)
                    }
                }
            }

        }
        backtrack("", next: digits)
        return result
    }
}

class Solution2 {
    func letterCombinations(_ digits: String) -> [String] {
        if digits.count == 0{
            return []
        }
         let numberPadDict = [
              "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
         ]
        var result = [String]()
        result.append("")
        for digit in digits{
            var tempResult = [String]()
            for firstChar in numberPadDict[String(digit)]!{
                for resultChar in result{
                    tempResult.append(resultChar+firstChar)
                }
            }
            result = tempResult
        }
        return result
    }
}
