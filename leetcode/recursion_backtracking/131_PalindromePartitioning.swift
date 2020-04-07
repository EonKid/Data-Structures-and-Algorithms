//https://leetcode.com/problems/palindrome-partitioning/submissions/


   class Solution {

    var arrResults = [[String]]()

    func isPalindrome(_ arrData: [Character]) -> Bool{
            var startIndex = 0
            var endIndex = arrData.count - 1
            while startIndex < endIndex{
                    if arrData[startIndex] != arrData[endIndex]{
                                return false
                    }
                    startIndex += 1
                    endIndex -= 1
            }
            return true
    }

    func dfs(_ startIndex: Int, _ arrCombinations: inout [String], _ arrData: [Character]){
                if startIndex >= arrData.count  {
                    arrResults.append(arrCombinations)
                }
                for i in startIndex ..< arrData.count {
                    let arrCurrent = arrData[startIndex...i]
                    if isPalindrome(Array(arrCurrent)){
                        let subStr = String(arrCurrent)
                        arrCombinations.append(subStr)
                        dfs(i+1, &arrCombinations, arrData)
                        arrCombinations.removeLast()
                    }
                }
    }

    func partition(_ s: String) -> [[String]] {
        if s.count == 0 { return [[]] }
        var arrCombinations = [String]()
        let arrData = Array(s)
        dfs(0,&arrCombinations, arrData)
        return arrResults
    }

}