def findMissing(nums):
    n = len(nums)
    thSum = 0
    for i in range(1,n+1):
        thSum += i
    return thSum - sum(nums)

print findMissing([3,4,-1,1])