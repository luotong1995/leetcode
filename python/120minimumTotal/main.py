from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    if len(triangle) < 2:
        return triangle[0][0]
    m = len(triangle)
    dp = [[0] * len(triangle[-1]) for _ in range(m)]
    dp[0][0] = triangle[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]
    for i in range(1, m):
        for j in range(1, len(triangle[i])):
            if j == len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
    return min(dp[m - 1])


print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
