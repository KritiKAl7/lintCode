from collections import defaultdict
def minCost(costs):
    dp = []
    for i in range(len(costs)):
        dp.append([0,0,0])
    dp[0] = costs[0]

    for i in range(1, len(costs)):
        dp[i][0] = min(dp[i-1][1] + costs[i][0], dp[i-1][2] + costs[i][0])
        dp[i][1] = min(dp[i-1][0] + costs[i][1], dp[i-1][2] + costs[i][1])
        dp[i][2] = min(dp[i-1][0] + costs[i][2], dp[i-1][1] + costs[i][2])
    print dp
    return min(dp[-1])

print minCost([[3,5,3],[6,17,6],[7,13,18],[9,10,18]])