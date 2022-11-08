'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。


输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1




输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3



'''
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count


def inArea(grid, r, c):
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
        return True
    else:
        return False


def dfs(g, r, c):
    if not inArea(g, r, c):
        return

    # 假设访问过后变成2， 不是岛屿也不能遍历
    if g[r][c] == '2' or g[r][c] == '0':
        return
    # 访问
    g[r][c] = 2
    dfs(g, r + 1, c)
    dfs(g, r, c + 1)
    dfs(g, r - 1, c)
    dfs(g, r, c - 1)


def DFS(g, v, visit):
    visit[v] = True
    print(v)
    w = neb(g, v, visit)
    while w >= 0:
        if not visit[w]:
            DFS(g, w, visit)
        w = neb(g, w, visit)


def neb(g, v, visit):
    for i in range(len(g)):
        if g[v][i] == "1" and not visit[i]:
            return i
    return -1


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(numIslands(grid))
