'''
给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。

返回执行此操作后，grid 中最大的岛屿面积是多少？

岛屿 由一组上、下、左、右四个方向相连的 1 形成。


示例 1:

输入: grid = [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
示例 2:

输入: grid = [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。
示例 3:

输入: grid = [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。
'''
from typing import List

arrow = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def largestIsland(grid: List[List[int]]) -> int:
    area = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                area.append(dfs(grid, i, j, len(area) + 2))

    if len(area) == 0:
        return 1

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                s = set()
                for item in arrow:
                    x = i + item[0]
                    y = j + item[1]
                    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid) and grid[x][y] != 0:
                        s.add(grid[x][y])
                ans = max(ans, sum(area[idx - 2] for idx in s) + 1)
            else:
                continue
    return ans if ans else len(grid) * len(grid)


# 查看ij周围的岛的面积
def dfs(grid: List[List[int]], i, j, tag):
    grid[i][j] = tag
    size = 1
    for item in arrow:
        x = i + item[0]
        y = j + item[1]
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid) and grid[x][y] == 1:
            size += dfs(grid, x, y, tag)

    return size


if __name__ == '__main__':
    grid = [[1, 0], [0, 1]]
    print(largestIsland(grid))
    print(grid)
