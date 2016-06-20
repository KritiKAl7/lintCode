#https://en.wikipedia.org/wiki/Dutch_national_flag_problem
def sortColors(nums):
    mid = 1
    midStart = 0 
    #right bound of numbers smaller than mid
    midEnd = len(nums) - 1 
    #right bound of nums bigger than mid
    index = 0

    while index <= midEnd:
        if nums[index] < mid:
            nums[midStart],nums[index] = nums[index],nums[midStart]
            index += 1
            midStart += 1
        elif nums[index] > mid:
            nums[midEnd],nums[index] = nums[index],nums[midEnd]
            midEnd -= 1
        else:
            index += 1
    return nums

print sortColors([0,1,2])

