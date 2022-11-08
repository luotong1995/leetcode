import sys


# 大数乘法
def solution(a, b):
    l = []
    for item in a:
        l.append(int(item))
    l.reverse()
    r = []
    for item in b[:-1]:
        r.append(int(item))
    r.reverse()
    z = [0] * 210
    for i in range(len(a)):
        for j in range(len(b) - 1):
            z[i + j] = z[i + j] + l[i] * r[j]
    for i in range(200):
        if z[i] >= 10:
            z[i + 1] = z[i + 1] + z[i] // 10
            z[i] = z[i] % 10

    k = 0
    for i in range(200, 0, -1):
        if z[i] == 0:
            continue
        else:
            k = i
            break
    s = ''
    while k >= 0:
        s += str(z[k])
        k -= 1
    print(s)


for line in sys.stdin:
    a = line.split(' ')
    solution(a[0], a[1])
