#http://www.cnblogs.com/65702708/archive/2010/09/14/1826362.html
#http://www.cnblogs.com/easonliu/p/4504647.html
def countOfplane(airplanes):
    L = []
    for i in range(len(airplanes)):
        L.append([airplanes[i][0], 1])
        L.append([airplanes[i][1], -1])
    #sort by time (if time equals, landing is in front of departing)
    L = sorted(L, cmp = lambda x, y: compare(x, y)) 
    counter = 0
    maxNum = 0
    print L
    lastN = 0
    for i in L:
        counter += i[1]
        lastN = i[0]
        maxNum = max(counter, maxNum)
    return maxNum

def compare(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] > y[1]:
            return 1
        else:
            return -1

#Slow AF
def countOfAirplanesB(self, airplanes):
    if not airplanes:
        return 0
    d = Counter()
    for i in airplanes:
        for j in range(i.start, i.end):
            d[j] += 1
    maxKey = max(d, key = d.get)
        return d[maxKey]
print countOfplane([[1,10],[2,3],[5,8],[4,7]])