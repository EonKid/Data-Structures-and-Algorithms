
import Foundation

class Solution {


    func powerVal(_ base: Int, _ n: Int) -> Int {
        if n == 0 {
            return 1
        }

        return base << (n - 1)
    }

    func getNumberFromCode(_ numStr: String, _ n: Int) -> Int{
        let arrData = Array(numStr)
            var counter = n - 1
            var number = 0
            for num in arrData{
                 let strData = String(num)
                guard let numData = Int(strData) else { return 0 }
                let multiplier = self.powerVal(2, counter)
                let result = numData * multiplier
                number = number + result
                counter -= 1
            }
            return number
    }

    func differsByOneBit(_ num1: Int, _ num2: Int) -> Bool{
         let bitDifference = num1 ^ num2
         return bitDifference != 0 && (bitDifference & (bitDifference - 1)) == 0
    }

    func backtrack(_ n: Int, _ historySet: inout Set<Int>, _ arrResult: inout [Int]) -> Bool {
        if arrResult.count == 1 << n{
            return differsByOneBit(arrResult.first!, arrResult.last!)
        }
        for i in 0 ..< n{
            let currentNum = arrResult.last!
            let mask = 1 << i
            let nextNum = currentNum ^ mask
            if !historySet.contains(nextNum) {
                arrResult.append(nextNum)
                historySet.insert(nextNum)
                if backtrack(n, &historySet, &arrResult){
                    return true
                }
                arrResult.removeLast()
                historySet.remove(nextNum)
            }
        }
        return false
    }

    func iterative(_ n: Int) -> [Int]{
            if n == 0{ return [0] }
            var arrData = ["0", "1"]
            var arrResult = [Int]()
            for _ in 0 ..< n - 1{
                     for num in arrData.reversed(){
                          arrData.append(num)
                    }
                    let midIndex = arrData.count / 2

                    for i in 0 ..< arrData.count{
                         var charToPlace = ""
                         if i < midIndex{
                               charToPlace  = "0"
                        }else{
                              charToPlace = "1"
                        }
                        let numChar = charToPlace + arrData[i]
                         arrData[i] = numChar
                    }
                }
              for numStr in arrData{
                let num = self.getNumberFromCode(numStr,n)
                    arrResult.append(num)
              }

            return arrResult
    }

    func recursion_optimal(_ n: Int) -> [Int] {
        if n == 0{
            return [0]
        }
        var arrResult = recursion_optimal(n - 1)
        let leadingOne = 1 << (n - 1)
        for num in arrResult.reversed(){
            arrResult.append(leadingOne | num)
        }
        return arrResult
    }

    func grayCode(_ n: Int) -> [Int] {

        /*
        var historySet = Set<Int>()
        historySet.insert(0)
        var arrResult = [Int]()
        arrResult.append(0)
        backtrack(n, &historySet, &arrResult)
        return arrResult
        */
        return recursion_optimal(n)
    }

}

let sol = Solution()
print(sol.grayCode(1))