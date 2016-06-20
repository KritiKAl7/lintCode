def numDistinct(S, T):
        # write your code here
        dp = []
        if len(S) < len(T):
        	return 0
        for i in range(len(S)+1):
            dp.append([0]*(len(T)+1))
        for i in range(len(S)+1):
        	dp[i][0] = 1
        print dp

        for i in range(1,len(S) + 1):
        	for j in range(1,len(T) + 1):
        		if S[i-1] == T[j-s1]:
        			dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        		else:
        			dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
print numDistinct("rabbbit","rabbit")
        
