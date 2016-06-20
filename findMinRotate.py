def findMinRotate(num):
	start = 0
	end = len(num) - 1
	
    while start < end:
    	mid = start + (end - start) / 2
		if num[mid] > num[end]:
		    start = mid + 1
	    elif num[mid] < num[end]:
	    	end = mid
	return num[mid]

print findMinRotate([-1,0,1,2,3,4,5,6,7,8])