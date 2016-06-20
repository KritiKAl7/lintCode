def maxSubarry(num):
    localMax = 0
    localMin = 0
    maxRes = 0

    for i in range(len(num)):
        tempMax = localMax
        localMax = max(localMax * num[i], localMin * num[i], num[i])
        localMin = min(tempMax * num[i], localMin * num[i], num[i])
        maxRes = max(maxRes, localMax)
    return maxRes

print maxSubarry([2,3,4,5,-6,10,-20])