import copy
from math import sqrt
import random
# http://jerrellguo.com/2016/01/08/leetcode-maximal-square/
def maxSquare(matrix):
    dp = [[0] * len(matrix[0]) for x in range(len(matrix))]
    for i in range(len(matrix[0])):
        if matrix[0][i] == 1:
            dp[0][i] = 1
    for j in range(len(matrix)):
        if matrix[j][0] == 1:
            dp[j][0] = 1
    
    maxSq = 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = 0
    maxSq = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            maxSq = max(maxSq, dp[i][j])
    return maxSq ** 2
