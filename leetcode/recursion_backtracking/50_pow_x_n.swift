// https://leetcode.com/problems/powx-n/

class Solution {


    func helper(_ x: Double, _ n: Int, _ end: Int)-> Double{
         if end == 0 {
            return 1.0
         }else{
            if n < 0{
                let half = helper(x,n,end/2)
                if end%2 == 0{
                   return half * half
                }else{
                   return (1/x) * half * half
                }

            }else{
                let half = helper(x,n,end/2)
                if end%2 == 0{
                   return half * half
                }else{
                    return x * half * half
                }

            }
         }
    }


    func myPow(_ x: Double, _ n: Int) -> Double {
         return helper(x,n,abs(n))
    }

}