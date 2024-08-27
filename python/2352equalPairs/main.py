from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    n = len(grid)
    rows = []
    cols = []
    res = 0
    for i in range(n):
        rows.append(grid[i])
    for i in range(n):
        cols.append([grid[j][i] for j in range(n)])
    for i in range(n):
        for j in range(n):
            if equal(rows[i], cols[j]):
                res += 1
    return res


def equalPairs2(grid: List[List[int]]) -> int:
    n = len(grid)
    rows = []
    cols = []
    a_dict = {}
    res = 0
    for i in range(n):
        rows.append(grid[i])
    for i in range(n):
        cols.append([grid[j][i] for j in range(n)])

    for item in rows:
        key = ','.join([str(i) for i in item])
        a_dict[key] = a_dict.get(key, 0) + 1

    for item in cols:
        key = ','.join([str(i) for i in item])
        if key in a_dict:
            res += a_dict[key]

    return res


def equal(rows, cols):
    for i in range(len(rows)):
        if rows[i] != cols[i]:
            return False
    return True


# print(equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
# print(equalPairs2([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(equalPairs2([[11, 1], [1, 11]]))
