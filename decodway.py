def numDecodings(s):
        # Write your code here
        dp = [1] * len(s)
        if not s:
            return 0
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        

        if len(s) == 2:
            if int(s) <= 26 and s[1] != "0":
                return 2
            else:
                return 1
        
        for i in range(1, len(dp)):
            dp[i] = 0
            if int(s[i]) > 0:
                dp[i] = dp[i-1]
            if 10 <= int(s[i-1] + s[i]) <= 26:
                dp[i] += dp[i-2]
        return dp

print numDecodings("508")