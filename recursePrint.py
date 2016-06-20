def numbersByRecursion(n):
    # write your code here
    return recurse([], n)
        
def recurse(res, n):
    if n == 1:
        return [1,2,3,4,5,6,7,8,9]
    else:
        res = recurse(res, n-1)
        newRes = []
        for i in res[10**(n-2) - 1:]:
            for j in range(10):
                newRes.append(i*10 + j)
        res.extend(newRes)
        return res

print numbersByRecursion(2)