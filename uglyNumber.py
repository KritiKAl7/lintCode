#http://www.cnblogs.com/grandyang/p/4743837.html
def uglyNumber(n):
    i2 = 0
    i3 = 0
    i5 = 0
    res = [1]
    while len(res) < n:
        m2 = res[i2] * 2
        m3 = res[i3] * 3
        m5 = res[i5] * 5
        minN = min(m2, m3, m5)
        if minN == m2:
            i2 += 1
        elif minN == m3:
            i3 += 1
        elif minN == m5:
            i5 += 1
        if res[-1] == minN:
            #one more step if repeats
            continue
        res.append(minN)
        i += 1
        print res
    return res[-1]

print uglyNumber(20)