'''
3184 构成整天的下标对数目I
给你一个整数数组 hours，表示以 小时 为单位的时间，返回一个整数，表示满足 i < j 且 hours[i] + hours[j] 构成 整天 的下标对 i, j 的数目。

整天 定义为时间持续时间是 24 小时的 整数倍 。

例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。

 

示例 1：

输入： hours = [12,12,30,24,24]

输出： 2

解释：

构成整天的下标对分别是 (0, 1) 和 (3, 4)。

示例 2：

输入： hours = [72,48,24,3]

输出： 3

解释：

构成整天的下标对分别是 (0, 1)、(0, 2) 和 (1, 2)。


思考：
第一种方法直接暴力求解
第二种方法：这里想要得到两个数的和为24，那么hours[i] + hours[j] = 24k，k >= 1，k为 constants，反过来说。
对于hours[j]，需要找到i的左边有多少个j满足hours[i]%24 = (24-hours[j]%24)%24。这里的i<j,想要通过hashmap来快速 COUNT，使用了HashMap。
直接对hours进行迭代，从index的小到大，然后使用hastmap来存储当前hours[j]%24是多少， 然后对hashmap进行count计数。计数的值为hashmap[hours[j]%24] += 1.
由于题目要去一共有多少个两个数的和为24，每次迭代的时候去hashmap中查询(24-hours[j]%24)%24的数量有多少，ans+= hashmap[(24-hours[j]%24)%24]。更新hashmap[hours[j]%24] += 1.
'''

from typing import List



def countCompleteDayPairs(hours: List[int]) -> int:
    ans = 0
    for i in range(len(hours)):
        for j in range(i+1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                ans += 1
    return ans


def countCompleteDayPairs2(hours: List[int]) -> int:
    ans = 0
    cnt=[0]*24
    for item in hours:
        ans += cnt[(24- item%24)%24]
        cnt[item%24] += 1
    return ans

hours = [12,12,30,24,24]
hours = [72,48,24,3]
print(countCompleteDayPairs2(hours))



1