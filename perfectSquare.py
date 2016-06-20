from math import sqrt
import sys
def perfectSquare(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        minRes = sys.maxint
        for j in range(1, int(sqrt(i)) + 1):
            square = j ** 2
            minRes = min(minRes, dp[i - square])
        dp[i] = minRes + 1
    return dp[-1]

def perfectSquareB(n):
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    for a in range(int(sqrt(n))):
        b = sqrt(n - a ** 2)
        if a*a + b*b == n:
            if a > 0 and b <= 0:
                return 1
            if a <= 0 and b > 0:
                return 1
            if a > 0 and b > 0:
                return 2
    return 3


print perfectSquareB(16)
