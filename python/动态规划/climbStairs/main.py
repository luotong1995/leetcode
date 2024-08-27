def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = [0] * n

    result[0] = 1
    result[1] = 2
    for i in range(n):
        if i > 1:
            result[i] = result[i - 1] + result[i - 2]
    return result[n - 1]


print(climbStairs(1))
