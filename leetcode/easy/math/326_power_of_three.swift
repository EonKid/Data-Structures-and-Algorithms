
/*

326. Power of Three


https://leetcode.com/problems/power-of-three/

*/

class Solution {
    func isPowerOfThree(_ n: Int) -> Bool {
        var number = n
        if n < 1{
            return false
        }
        while number % 3 == 0{
            number = number / 3
            
        }
        if number == 1{
            return true
        }
        return false
    }
}