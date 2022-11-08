# coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys

# 1990-01-01这天开始是三天打鱼两天晒网，给一个日期判断是在干嘛

def run(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    return False


def solution(y, m, d):
    if y < 1990:
        print('Invalid input')
        return
    if m < 1 or m > 12:
        print('Invalid input')
        return
    if d < 1:
        print('Invalid input')
        return
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        if d > 29:
            print('Invalid input')
            return
    else:
        if d > 28:
            print('Invalid input')
            return
    month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    s_m = 0
    for i in range(1, m):
        s_m += month[i]
    if run(y):
        if m > 2:
            s_m += 1
    s_y = 0
    for i in range(1990, y):
        if run(i):
            s_y += 1
    s_d = s_y + s_m + d
    a = s_d % 5
    if a == 0:
        print('He is having a rest')
    elif a == 1:
        print('He is working')
    elif a == 2:
        print('He is working')
    elif a == 3:
        print('He is working')
    elif a == 4:
        print('He is having a rest')
    return


for line in sys.stdin:
    a = line.split('-')
    solution(int(a[0]), int(a[1]), int(a[2]))

