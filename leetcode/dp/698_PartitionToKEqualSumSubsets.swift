// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution {

    func canPartitionKSubsets(_ nums: [Int], _ k: Int) -> Bool {
		  let sumOfNums = nums.reduce(0, +)
		  if sumOfNums % k != 0{
			return false
		  }
         var arrData = nums
		 let target = sumOfNums / k
		 var arrVisited = Array.init(repeating: false, count: nums.count)
		 arrData.sort()
		 return dfs(arrData, &arrVisited, k, 0, target, nums.count - 1)

    }

	func dfs(_ nums: [Int], _ arrVisited: inout [Bool], _ k: Int, _ sum: Int, _ target: Int, _ index: Int) -> Bool{

		if k == 0 {
			return true
		}

		if sum == target{
			return dfs(nums, &arrVisited, k - 1, 0, target, nums.count - 1)
		}

		for i in stride(from: index, to: -1, by: -1){

				if arrVisited[i] || sum + nums[i] > target{
						continue
				}
				arrVisited[i] = true
				if dfs(nums, &arrVisited, k, sum + nums[i], target, i - 1){
					return true
				}

				arrVisited[i] = false
		}

		return false

	}

}