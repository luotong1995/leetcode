def uniquePaths(m: int, n: int) -> int:
    path = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        row = []
        for j in range(n):
            row.append(0)
        path.append(row)

    for i in range(m):
        path[i][0] = 1

    for i in range(n):
        path[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            path[j][i] = path[j][i - 1] + path[j - 1][i]

    return path[m - 1][n - 1]


print(uniquePaths(3, 2))
