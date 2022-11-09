def dfs(n, l, result, tl):
    if n == len(l):
        result.append(list(tl))
        return
    tl.append(l[n])
    dfs(n + 1, l, result, tl)
    tl.pop()
    dfs(n + 1, l, result, tl)


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    res = []
    tl = []
    dfs(0, a, res, tl)
    print(res)
