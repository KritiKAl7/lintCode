import math
def numTrees(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        for j in range(0, i):
            """
            for a tree with i nodes
            the total number of possible trees
            is the sum of the product of all possible 
            subtrees
            for example dp[4] = 
            dp[0]*dp[3] + dp[1]*dp[2] + dp[2]*dp[1]
            + dp[3]*dp[0]
            """
            dp[i] += dp[j] * dp[i-j-1]
            print i, j, i-j-1
    return dp[-1]

def numTreeCatalanNum(n):
    """
    catalan number:
    n = 2n!/(n!*n!) * 1/(n+1)
    """
    return (math.factorial(2 * n) / 
        (math.factorial(n) ** 2) / (n+1))


print numTreeCatalanNum(4)
