'''
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。


输入：timePoints = ["23:59","00:00"]
输出：1

输入：timePoints = ["00:00","23:59","00:00"]
输出：0
'''

0, 3, 1439
-1440, -1437, -1
from typing import List


def findMinDifference(timePoints: List[str]) -> int:
    num = []

    for item in timePoints:
        h, m = int(item[:2]), int(item[-2:])
        a = h * 60 + m
        num.append(a)
    num.sort()
    m = min(abs(num[0] - num[-1]), abs(num[0] + 1440 - num[-1]))
    for i in range(len(num)):
        if i + 1 < len(num):
            if abs(num[i + 1] - num[i]) < m:
                m = abs(num[i + 1] - num[i])
    return m


if __name__ == '__main__':
    print(findMinDifference(["23:59", "00:00"]))
