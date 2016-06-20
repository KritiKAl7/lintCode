def removeDuplicateSorted(A):
    i = 0
    j = 1
    while i < len(A) and j < len(A):
        if A[i] == A[j]:
            while j < len(A) and A[i] == A[j]:
                j += 1
            del A[i+1:j]
            j = i + 1
        else:
            i += 1
            j += 1
    return len(A)

print removeDuplicateSorted([1,1,1,2,3,3,3,3,4,4])
