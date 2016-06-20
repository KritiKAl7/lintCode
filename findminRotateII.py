def findMinR(nums):
    return findMinRotate(nums, 0, len(nums) - 1)

def findMinRotate(nums, start, end):
    if start == end:
        return nums[start]
    mid = start + (end - start) / 2
    if nums[mid] > nums[end]:
        return findMinRotate(nums, mid+1, end)
    elif nums[mid] < nums[end]:
        return findMinRotate(nums, start, mid)
    elif nums[mid] == nums[end]:
        left = findMinRotate(nums, start, mid)
        right = findMinRotate(nums, mid+1, end)
        return min(left, right)

print findMinR([4,4,5,6,7,8,8,1,2,3])