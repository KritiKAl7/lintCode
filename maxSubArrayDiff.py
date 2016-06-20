def maxSubDifference(nums):
    #the two subarrays must be adjacent because
    #one of the subarrays can always include
    #the number in between.
    maxDiff = 0
    maxL = [0] * len(nums)
    minL = [0] * len(nums)
    maxR = [0] * len(nums)
    minR = [0] * len(nums)

    #max and min subarray from left to right
    maxL[0], minL[0] = nums[0], nums[0]
    #max and min subarray from right to left
    maxR[-1], minR[-1] = nums[-1], nums[-1]

    for i in range(1, len(nums)):
        maxL[i] = max(maxL[i-1] + nums[i], nums[i])
        minL[i] = min(minL[i-1] + nums[i], nums[i])
    for i in range(len(nums) - 2, -1, -1):
        maxR[i] = max(maxR[i+1] + nums[i], nums[i])
        minR[i] = min(minR[i+1] + nums[i], nums[i])
    for i in range(len(nums) - 1):
        maxDiff = max(maxDiff, abs(maxL[i]-minR[i+1]), 
            abs(maxR[i+1]-minL[i]))
    return maxDiff

print maxSubDifference([1,2,-3,1])