"""

nums = [2, 3, 7]
target = 12

"""

def score_combination2(nums: [int], target: int):
    dp = [0]*(target+1)
    dp[0] = 1
    for num in nums:
        for i in range(1, target+1):
            if i >= num:
                dp[i] += dp[i-num]
    return dp[target]

def score_combinations(nums: [int], target: int):
    dp = [[0]*(target+1) for _ in range(len(nums))]
    for i in range(0, len(nums)):
        dp[i][0] = 1
        for j in range(1, target+1):
            if i - 1 >= 0:
                withThis = dp[i-1][j]
            else:
                withThis = 0
            if j >= nums[i]:
                withoutThis = dp[i][j - nums[i]]
            else:
                withoutThis = 0
            dp[i][j] = withThis + withoutThis
    return dp[len(nums) - 1][target]

print("COUNT THE NUMBER OF SCORE COMBINATIONS #0: ", score_combinations([2,3,7], 12))
print("COUNT THE NUMBER OF SCORE COMBINATIONS #1: ", score_combination2([2,3,7], 12))