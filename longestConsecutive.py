def longestConsecutive(num):
    if not num:
        return 0
    d = {}
    maxLength = 1
    for i in num:
        d[i] = True
    for i in num:
        if d[i] == True:
            length = 1
            for left in range(i - 1, i - len(num), -1):
                if left in d:
                    length += 1
                    d[left] = False
                else:
                    break
            for right in range(i + 1, i + len(num), 1):
                if right in d:
                    length += 1
                    d[right] = False
                else:
                    break
            maxLength = max(maxLength, length)
    return maxLength

print longestConsecutive([2,3,5,1,3,4])


