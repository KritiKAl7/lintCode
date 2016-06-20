def longestIncreasingSubsequenceA(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def longestIncreasingSubsequenceB(nums):


print longestIncreasingSubsequenceA([5,4,1,0,2,3,4,5,6,1])
