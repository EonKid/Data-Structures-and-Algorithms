// https://leetcode.com/problems/partition-equal-subset-sum/

class Solution {
    func canPartition(_ nums: [Int]) -> Bool {
        let k = 2
        if nums.count == 0 || nums.count < 2{
            return false
        }
        let sumOfNums = nums.reduce(0, +)
		  if sumOfNums % k != 0{
			return false
		  }
         var arrData = nums
		 let target = sumOfNums / k
         if arrData.max() ?? 0 > target{ return false }
		 arrData.sort()
		 return dfs(arrData, 0, target, nums.count - 1)
    }

    func dfs(_ nums: [Int], _ sum: Int, _ target: Int, _ index: Int) -> Bool{

		if sum == target{
			return true
		}

		for i in stride(from: index, to: -1, by: -1){

				if  sum + nums[i] > target{
						continue
				}
				if dfs(nums, sum + nums[i], target, i - 1){
					return true
				}
		}
		return false
	}
}