
'''

给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 升序排列 。计算并返回该研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）至少 有 h 篇论文分别被引用了至少 h 次。

请你设计并实现对数时间复杂度的算法解决此问题。

 

示例 1：

输入：citations = [0,1,3,5,6]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
     由于研究者有3篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。
示例 2：

输入：citations = [1,2,100]
输出：2
 

提示：

n == citations.length
1 <= n <= 105
0 <= citations[i] <= 1000
citations 按 升序排列

思考：
找到满足有x篇论文被引用x次的最大值，即找到数组中

假设我们在一个升序数组中，寻找满足某个条件的最大值。下面的示例是寻找数组中`最后一个小于等于`目标值的元素。

'''



from typing import List


def hIndex(citations: List[int]) -> int:
    left, right = 1, len(citations)
    while left <= right:
        mid = (left + right) // 2
        if sum([1 if item >= mid else 0 for item in citations]) >= mid:  # 满足条件，尝试找到更大的位置，尝试向右找更大的解
            left = mid + 1  # 增大左边界
        else: #nums[mid] > target，缩小范围
            right = mid - 1  # 收缩右边界
    return right

citations = [1,2,100]
# citations = [0,1,3,5,6]
print(hIndex(citations))
        