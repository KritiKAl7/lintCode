def rearrangeA(L):
    posN = 0
    negN = 0
    for i in L:
        if i > 0:
            posN += 1
        else:
            negN += 1
    if posN > negN:
        posIn = 0
        negIn = 1
    else:
        posIn = 1
        negIn = 0
    while posIn < len(L) and negIn < len(L):
        while posIn < len(L) and L[posIn] > 0:
            posIn += 2
        while negIn < len(L) and L[negIn] < 0:
            negIn += 2
        if posIn < len(L) and negIn < len(L):
            L[posIn], L[negIn] = L[negIn], L[posIn]
            posIn += 2
            negIn += 2
    return L
print rearrangeA([28,2,-22,-27,2,9,-33,-4,-18,26,25,34,-35,-17,2,-2,32,35,-8])
