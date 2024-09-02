"""
给你一个长度为 n 的二维整数数组 items 和一个整数 k 。

items[i] = [profiti, categoryi]，其中 profiti 和 categoryi 分别表示第 i 个项目的利润和类别。

现定义 items 的 子序列 的 优雅度 可以用 total_profit + distinct_categories2 计算，其中 total_profit 是子序列中所有项目的利润总和，distinct_categories 是所选子序列所含的所有类别中不同类别的数量。

你的任务是从 items 所有长度为 k 的子序列中，找出 最大优雅度 。

用整数形式表示并返回 items 中所有长度恰好为 k 的子序列的最大优雅度。

注意：数组的子序列是经由原数组删除一些元素（可能不删除）而产生的新数组，且删除不改变其余元素相对顺序。


示例 1：

输入：items = [[3,2],[5,1],[10,1]], k = 2
输出：17
解释：
在这个例子中，我们需要选出长度为 2 的子序列。
其中一种方案是 items[0] = [3,2] 和 items[2] = [10,1] 。
子序列的总利润为 3 + 10 = 13 ，子序列包含 2 种不同类别 [2,1] 。
因此，优雅度为 13 + 22 = 17 ，可以证明 17 是可以获得的最大优雅度。
示例 2：

输入：items = [[3,1],[3,1],[2,2],[5,3]], k = 3
输出：19
解释：
在这个例子中，我们需要选出长度为 3 的子序列。
其中一种方案是 items[0] = [3,1] ，items[2] = [2,2] 和 items[3] = [5,3] 。
子序列的总利润为 3 + 2 + 5 = 10 ，子序列包含 3 种不同类别 [1, 2, 3] 。
因此，优雅度为 10 + 32 = 19 ，可以证明 19 是可以获得的最大优雅度。
示例 3：

输入：items = [[1,1],[2,1],[3,1]], k = 3
输出：7
解释：
在这个例子中，我们需要选出长度为 3 的子序列。
我们需要选中所有项目。
子序列的总利润为 1 + 2 + 3 = 6，子序列包含 1 种不同类别 [1] 。
因此，最大优雅度为 6 + 12 = 7 。
"""
from typing import List


##
# 按照利润从大到小排序，找出前K个元素，计算出profit，然后使用栈记录下来类别重复的元素，因为利润是按照从大到小排序的，所以，栈顶的元素一直十最小的
# 需要巧妙的用到单调栈的思想，一直找出栈顶的元素最小，然后遍历从k+1-n的元素，如果元素类别，在候选集中没有出现，可以替换，但是需要考虑候选集中的元素类别是否有重复，如果有重复才替换，没有重复，替换则会导致结果变小，则不需要替换

def findMaximumElegance(items: List[List[int]], k: int) -> int:
    items.sort(key=lambda item: -item[0])
    category = set()
    ans, profit = 0, 0
    # stack
    duplicate = []
    for i, item in enumerate(items):
        if i < k:
            profit += item[0]
            if item[1] in category:
                duplicate.append(item[0])
            else:
                category.add(item[1])
        else:
            if item[1] not in category and len(duplicate) > 0:
                profit += item[0] - duplicate.pop()
                category.add(item[1])
        ans = max(ans, profit + len(category) ** 2)
    return ans


def getElegance(datas: List[List[int]]) -> int:
    total_profilt = sum([item[0] for item in datas])
    categories = set()
    for item in datas:
        categories.add(item[1])

    return total_profilt + len(categories) ** 2


if __name__ == '__main__':
    items = [[3, 2], [5, 1], [10, 1]]
    print(findMaximumElegance(items, 2))
