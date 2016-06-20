def heapify(L):
    for i in range(len(A), 0, -1):
        percUp(i, A)
    return A

def percUp(i, L)
    lKid = L[2*i+1]
    rKid = L[2*i+2]
    if lKid <= rKid:
        minIndex = 2*i+1
    else:
        minIndex = 2*i+2
    if max(lKid, rKid) < L[i]:
        temp = L[i]
        L[i] = L[minIndex]
        L[minIndex] = temp
        percUp(minIndx, L)

print heapify([3,2,1,4,5,7,6])