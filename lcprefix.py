def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    
    first = strs[0]
    count = compare(first, strs[1])
    for s in strs[1:]:
        count = min(count, compare(first, s))
    return strs[1][:count]



def compare(a, b):
    length = min(len(a), len(b))
    count = 0
    for i in xrange(length):
        if a[i] == b[i]:
            count += 1
        else:
            break
    return count

print longestCommonPrefix(["BCD","BEF","CEF"])