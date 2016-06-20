import random
def minimumSize(nums, s):
    if sum(nums) < s:
        return -1
    i = 0
    j = 1
    minLen = len(nums)
    while i < j and j <= len(nums):
        if sum(nums[i:j]) >= s:
            minLen = min(minLen, j - i)
            i += 1
        else:
            j += 1
    print i, j, nums[i:j]
    return minLen

def tst():
    L =[]
    for i in range(10):
        L.append(random.randint(5,25))
    print L, random.randint(10,sum(L) * 2)

for i in xrange(10):
    tst()

print minimumSize([20, 21, 25, 15, 5, 25, 16, 24, 17, 18], 150)