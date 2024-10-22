'''
1011 在D天内送达包裹的能力

传送带上的包裹必须在 days 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量（weights）的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], days = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
示例 2：

输入：weights = [3,2,2,4,1,4], days = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
示例 3：

输入：weights = [1,2,3,1,1], days = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
 

提示：

1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500


思考：
首先这里的目标是要在days之内送达所有的包裹，所以这个条件是必须满足的。然后我们要求的是船的最低运载能力。
这里我们需要找到能够成功在days之内送达所有包裹的运载能力的，左右边界。
右边界：所有物品重量的和sum(weights)
左边界：所有物品重量的和sum(weights)// days，理想情况，让每天都运满，即可得到最小的运载能力。所以这个事左边界
然后使用二分查找，查找第一个满足条件的运载能力，即为最低运载能力

'''

from typing import List


def count_days(weights, coverage):
    ans = 0
    temp = 0
    i = 0
    while i < len(weights):
        if (temp + weights[i])  == coverage:
            ans += 1
            temp = 0
        elif (temp + weights[i]) > coverage:
            ans += 1
            temp = weights[i]            
        else:
            temp += weights[i]
        i += 1
    if temp > 0:
        ans += 1
    return ans


def shipWithinDays(weights: List[int], days: int) -> int:
    total_weight  = sum(weights)
    left = total_weight // days
    right = total_weight
    max_value = max(weights)
    while left <= right:
        mid = (left + right) // 2

        if mid < max_value or count_days(weights,  mid) > days:
            left = mid + 1
        else:
            right = mid - 1
    return left

weights = [1,2,3,1,1]
days = 4
# print(count_days(weights, 2))

# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5

# weights = [3,2,2,4,1,4]
# days = 3
print(shipWithinDays(weights, days))