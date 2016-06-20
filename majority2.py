def majorityNum(L):
    candA = 0
    candB = 0
    countA = 0
    countB = 0
    for i in L:
        if i == candA:
            countA += 1
        elif i == candB:
            countB += 1
        elif countA == 0:
            candA = i
            countA += 1
        elif countB == 0:
            candB = i
            countB += 1
        else:
            countA -= 1
            countB -= 1
    countA, countB = 0, 0
    for i in L:
        if i == candA:
            countA += 1
        elif i == candB:
            countB += 1
            
    if countA > countB:
        return candA
    else:
        return candB



print majorityNum([1,1,1,1,2,2,3,3,4,4,4])