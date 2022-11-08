'''
给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。

返回执行此操作后，grid 中最大的岛屿面积是多少？

岛屿 由一组上、下、左、右四个方向相连的 1 形成。


输入: grid = [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。



输入: grid = [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。



输入: grid = [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。
'''
from typing import List


def dfs(g, r, c):
    if not inArea(g, r, c):
        return 0
    if g[r][c] != 1:
        return 0
    g[r][c] = 2
    return 1 + dfs(g, r + 1, c) + dfs(g, r, c + 1) + dfs(g, r - 1, c) + dfs(g, r, c - 1)


def inArea(g, r, c):
    if r >= 0 and r < len(g) and c >= 0 and c < len(g[0]):
        return True
    return False


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    m = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                m = max(m, dfs(grid, i, j))
    return m


def copy(grid):
    r = []
    for i in range(len(grid)):
        l = []
        for j in range(len(grid[0])):
            l.append(grid[i][j])
        r.append(l)
    return r


def largestIsland(grid: List[List[int]]) -> int:
    m = maxAreaOfIsland(copy(grid))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            a = copy(grid)
            if a[i][j] == 0:
                a[i][j] = 1
                m = max(m, maxAreaOfIsland(a))
    return m


if __name__ == '__main__':
    grid = [[1, 0], [0, 1]]
    print(largestIsland(grid))
