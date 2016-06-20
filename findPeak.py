def findPeak(A):
    start = 0
    end = len(A) - 1
    while start < end:
        mid = start + (end - start) / 2
        if A[mid] < A[mid+1]:
            start = mid + 1
        else:
            end = mid
    return mid

print findPeak([1,2,4,5,6,7,8,6])
