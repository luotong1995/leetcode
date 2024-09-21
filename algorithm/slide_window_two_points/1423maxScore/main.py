'''
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

 

示例 1：

输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
示例 2：

输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
示例 3：

输入：cardPoints = [9,7,7,9,7,7,9], k = 7
输出：55
解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
示例 4：

输入：cardPoints = [1,1000,1], k = 1
输出：1
解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。 
示例 5：

输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
输出：202
 

提示：

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length


思考：使用前后双指针来完成，每次拿都选择中间最大的数，直到满足k个数字为止, 测试发现这个事错的，比如[11,49,100,20,86,29,72]
按照刚刚的思想，得到的取的数字为72，29，86，20，结果为207，但是还可以取11，49，72，100，结果为232

再思考，想要取得数字和最大，那剩下的数字之和肯定最小且连续，最小且连续就是突破口，可以直接使用滑动窗口
'''


import math
from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    ans = 0
    n = len(cardPoints)
    total = sum(cardPoints)
    cur_sum = 0
    min_sum = math.inf
    if k == n:
        return total
    for i in range(n):
        cur_sum += cardPoints[i]
        if i < (n - k - 1):
            continue
        min_sum = min(min_sum, cur_sum)
        temp = i - n + k + 1
        cur_sum -= cardPoints[temp]
    ans = total - min_sum
    return ans
cardPoints = [9,7,7,9,7,7,9]

k = 7
# cardPoints = [1,2,3,4,5,6,1]
# k = 3
# cardPoints = [11,49,100,20,86,29,72]
# k = 4
print(maxScore(cardPoints, k))
