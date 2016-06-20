def longestNonRepeating(s):
    if not s:
        return 0
    maxLen = 1
    i = 0
    while i <= len(s):
        length = 0
        d = {}
        j = i
        breaked = False
        while j <= len(s) - 1:
            if s[j] in d:
                breaked = True
                break
            d[s[j]] = j
            length += 1
            j += 1
        maxLen = max(maxLen, length)
        if breaked:
            i = d[s[j]] + 1
        else:
            i = j + 1
    return maxLen

print longestNonRepeating("aab")