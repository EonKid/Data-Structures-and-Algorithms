// https://leetcode.com/problems/fibonacci-number/

class Solution {
    func fib(_ N: Int) -> Int {
        if N == 0{
            return 0
        }
        if N == 1{
            return 1
        }
        var arrFib = Array.init(repeating: 0, count: N+1)
        arrFib[0] = 0
        arrFib[1] = 1
        for i in 2 ..< N+1{
            arrFib[i] = arrFib[i-1] + arrFib[i-2]
        }
        return arrFib[N]
    }
}