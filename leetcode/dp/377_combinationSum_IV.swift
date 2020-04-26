
//https://leetcode.com/problems/combination-sum-iv/




class Solution {

    var dictCache = [Int: Int]()

    func solution4(_ nums: [Int], _ target: Int) -> Int{
          var dp = [Double](repeatElement(0,count: target+1))
          dp[0] = 1
          for i in 0 ..< target + 1{
                for num in nums{
                        if i >= num{
                            dp[i] += dp[i - num]
                        }
                }
          }
          return Int(dp[target])
    }

    func solution3(_ nums: [Int], _ target: Int) -> Int{

        if dictCache[target] != nil{
            return dictCache[target] ?? 0
        }

        if target == 0 {
            return 1
        }
        if target == 0{
            return 0
        }
        var result = 0

        for num in nums{
            guard target - num >= 0 else{ continue }
            result += solution3(nums, target - num)
        }

        dictCache[target] = result
        return result
    }

    func solution2(_ nums: [Int], _ target: Int, _ resultCount: inout Int){

            if target == 0{
                resultCount += 1
                return
            }

            if target < 0{
                 return
            }

            for i in 0 ..< nums.count{
                solution2(nums,target - nums[i], &resultCount)
            }

     }

    func solution1(_ nums: [Int], _ target: Int, _ combinations: inout [Int], _ arrResults: inout [[Int]]){
        if target == 0{
            arrResults.append(combinations)
            return
        }
        if target < 0{
            return
        }
        for i in 0 ..< nums.count{
                combinations.append(nums[i])
                solution1(nums, target - nums[i], &combinations,  &arrResults)
                combinations.removeLast()
        }

    }

    func combinationSum4(_ nums: [Int], _ target: Int) -> Int {

          // Solution 1
//          var arrResults = [[Int]]()
//          var combinations = [Int]()
//          solution1(nums, target, &combinations,  &arrResults)
//          return arrResults.count

         // Soltion 2
//        var resultCount = 0
//        solution2(nums,target,&resultCount)
//        return resultCount

        // Solution 3
//         return solution3(nums, target)

        //Solution 4
        return solution4(nums, target)

    }

}


