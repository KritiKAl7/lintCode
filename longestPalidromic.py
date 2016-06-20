def longestPalidrome(s):
    dp = [[False] * len(s) for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            if i >= j:
                dp[i][j] = True
    left, right = 0, 0
    for k in range(2, len(s) + 1): #the length of substring
        for i in range(len(s) - k + 1): #start of substring
            if s[i] == s[i+k-1] and dp[i+1][i+k-2]:
                dp[i][i+k-1] = True
                if right - left + 1 < k:
                    left = i
                    right = i+k-1
    return s[left:right+1]

print longestPalidrome("abcdzdcabc")

