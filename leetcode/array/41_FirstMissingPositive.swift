// https://leetcode.com/problems/first-missing-positive/

class Solution {
    func firstMissingPositive(_ nums: [Int]) -> Int {
        // return bruteForce(nums)
        return helperForLinear(nums)
    }

    /*
    Time: O(n)
    Space: O(1)
    */

    func helperForLinear(_ nums: [Int]) -> Int{
        var nums = nums
        let n = nums.count
        if n == 0{
            return 1
        }

        var containsOne = 0
        for i in 0 ..< n{
            if nums[i] == 1{
                containsOne = 1
            }else if nums[i] <= 0 || nums[i] > n{
                nums[i] = 1
            }
        }

        if containsOne == 0 {
            return 1
        }

        for i in 0 ..< n{
            let index = abs(nums[i]) - 1
            if nums[index] > 0{
                nums[index] = -1 * nums[index]
            }
        }

        for i in 0 ..< n{
            if nums[i] > 0{
                return i + 1
            }
        }

        return n + 1
    }

    /*
     Time: O(n)
     Space: O(n)
    */
    func bruteForce(_ nums: [Int]) -> Int{
          var store = Set<Int>()
		  for num in nums{
				store.insert(num)
		  }
		let n = nums.count + 1

		for i in 1 ..< n {
			if !store.contains(i){
					return i
			}
		}
		return n
    }
}