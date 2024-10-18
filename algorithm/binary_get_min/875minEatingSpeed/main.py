'''
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。

珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

 

示例 1：

输入：piles = [3,6,7,11], h = 8
输出：4
示例 2：

输入：piles = [30,11,23,4,20], h = 5
输出：30
示例 3：

输入：piles = [30,11,23,4,20], h = 6
输出：23
 

提示：

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9


思考：
首先这个题目需要在给定的h小时内吃掉所有的香蕉，只是这个会受到速度k的影响，想要求出最小速度k，k越小越没可能吃完所有的香蕉，k越大越容易完成任务。
由于速度是整数，所以一定是大于等于1，并且不能是无限大，需要找到最大的边界，然后从这个左右边界中，找到最小的速度满足情况。
就是找到第一个满足情况的速度，使用lowbound来实现

left = 1 or sum(piles) // h 即 math.ceil(sum(piles) / h)
right = max(piles)

'''


import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    # total_piles = sum(piles)
    left = math.ceil(sum(piles) / h)
    right = max(piles)
    while left <= right:
        mid = (left + right) // 2
        if sum([math.ceil(item/mid) for item in piles]) > h:
            left = mid + 1
        else:
            right = mid - 1
    return left
piles = [30,11,23,4,20]
h = 6
piles = [312884470]
h = 968709470
print(minEatingSpeed(piles, h))
312884470
968709470