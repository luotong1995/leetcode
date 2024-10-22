'''
2576 求出最多标记下标

给你一个下标从 0 开始的整数数组 nums 。

一开始，所有下标都没有被标记。你可以执行以下操作任意次：

选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。

 

示例 1：

输入：nums = [3,5,2,4]
输出：2
解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
没有其他更多可执行的操作，所以答案为 2 。
示例 2：

输入：nums = [9,2,5,4]
输出：4
解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
没有其他更多可执行的操作，所以答案为 4 。
示例 3：

输入：nums = [7,6,8]
输出：0
解释：没有任何可以执行的操作，所以答案为 0 。


思考：
最多标记的问题，第一想法还是用二分查找去找出，首先要先找出二分查找的范围；

容易发现，若我们能找到 k 对标记，那么一定能找到 k−1 对标记。若我们找不到 k 对标记，也一定找不到 k+1 对标记。因此答案具有单调性，可以使用二分求解。

首先二分枚举 m，然后尝试将最小的 m 个数字和最大的 m 个数字一一尝试匹配。这样做的原因在于，我们可以证明若能找到 m 对标记，那么最小的 m 个数字和最大的 m 个数字一定可以匹配。
使用反证法证明，若未匹配最小的 m 个数字和最大的 m 个数字，那么对于某对匹配 nums[i] 与 nums[j]，其中 2×nums[i]≤nums[j]，总会找到一个更小的 nums[i] 来替换 nums[i]，或找到一个更大的 nums[j] 来替换 nums[j]。

因此，首先对nums进行排序，然后将下标[0,m−1]范围内的每个nums[i]，与下标[n−m,n−1]范围内的每个nums[j]尝试进行匹配，其中nums[i]匹配nums[n−m+i]。若所有元素都可成功匹配，则判定可以找到m组匹配。

left = 0
right = n // 2


'''


from typing import List


def maxNumOfMarkedIndices(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    left = 0
    right =  n// 2

    def check(m):
        for i in range(m):
            if 2 * nums[i] > nums[n - m + i]:
                return False
        return True


    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right*2

nums = [7,6,8]
print(maxNumOfMarkedIndices(nums))
