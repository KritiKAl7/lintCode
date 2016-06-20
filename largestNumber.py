def largestNumber(num):
    for i in xrange(len(num)):
        num[i] = str(num[i])
    num = mergesort(num)
    res = "".join(num[::-1])
    if int(res) == 0:
        return "0"
        
    return res
        
def mergesort(L):
    if len(L) <= 1:
        return L
    mid = len(L) / 2
    left = mergesort(L[:mid])
    right = mergesort(L[mid:])
    return merge(left, right)
        
def merge(left, right):
    r, l = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if bigger(left[l], right[r]):
            res.append(right[r])
            r += 1
        else:
            res.append(left[l])
            l += 1
    res += right[r:]
    res += left[l:]
    return res   
            
def bigger(a, b):
    if int(a + b) > int(b + a):
        return True
    else:
        return False

print largestNumber([1,20,23,4,8])