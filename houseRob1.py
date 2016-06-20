def houseRobber(self, A):
    # write your code here
    if not A:
        return 0
    if len(A) == 1:
        return A[0]
    dp = [0] * len(A)
    dp[0] = A[0]
    dp[1] = max(A[0], A[1])
    for i in range(2, len(A)):
        dp[i] = max(dp[i-1], dp[i-2] + A[i])
    return dp[-1]