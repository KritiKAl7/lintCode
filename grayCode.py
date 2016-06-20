def grayCode(n):
    if n == 0:
        return []
    res = grayCodeN(n-1, ["0", "1"])
    solution = []
    for i in res:
        solution.append(int(i,2))
    return solution

def grayCodeN(n, prev):
    if n == 0:
        return prev
    else:
        res = []
        for i in range(0, len(prev), 2):
            a = prev[i]
            b = prev[i+1]
            ares = [a+"0", a+"1"]
            bres = [b+"1", b+"0"]
            res += ares
            res += bres
        return grayCodeN(n-1, res)

print grayCode(6)
