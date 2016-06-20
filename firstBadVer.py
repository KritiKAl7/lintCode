def findFirstBadVersion(self, n):
        # write your code here
    start = 1
    end = n
    mid = start + (end - start) / 2
    while start <= end:
        mid = start + (end - start) / 2
        if SVNRepo.isBadVersion(mid):
            if mid == 1 or not SVNRepo.isBadVersion(mid - 1):
                return mid
            else:
                end = mid
        else:
            start = mid + 1
               
    return mid   
