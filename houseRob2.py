def houseRobb2(A):
    if not A:
        return 0
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        return max(A[0], A[1])
    dpA = [0] * len(A)
    dpB = [0] * len(A)
    dpA[0] = A[0]
    dpA[1] = A[0]
    dpB[1] = A[1]

    for i in range(2,len(A) - 1):
        dpA[i] = max(dpA[i-1], dpA[i-2] + A[i])
        dpB[i] = max(dpB[i-1], dpB[i-2] + A[i])
    dpA[-1] = dpB[-2]
    dpB[-1] = dpB[-3] + A[-1]
    return max(max(dpA), max(dpB))

print houseRobb2([3,6,4,3,5,6,1,4,1,6,1,8,4,9,10,32])