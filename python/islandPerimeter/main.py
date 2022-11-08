'''
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
'''

from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(grid, i, j)


def dfs(grid, r, c):
    # 当到达边界则周长加一
    if not inArea(grid, r, c):
        return 1

    # 当到达水域的时候周长加一
    if grid[r][c] == 0:
        return 1

    # 当遍历过之后的陆地则不管
    if grid[r][c] != 1:
        return 0

    grid[r][c] = 2
    return dfs(grid, r + 1, c) + dfs(grid, r, c + 1) + dfs(grid, r - 1, c) + dfs(grid, r, c - 1)


def inArea(grid, r, c):
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
        return True
    return False


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(islandPerimeter(grid))
