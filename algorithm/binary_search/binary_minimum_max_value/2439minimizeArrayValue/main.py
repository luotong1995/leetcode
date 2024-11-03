'''
2439. 最小化数组中的最大值
给你一个下标从 0 开始的数组 nums ，它含有 n 个非负整数。

每一步操作中，你需要：

选择一个满足 1 <= i < n 的整数 i ，且 nums[i] > 0 。
将 nums[i] 减 1 。
将 nums[i - 1] 加 1 。
你可以对数组执行 任意 次上述操作，请你返回可以得到的 nums 数组中 最大值 最小 为多少。

 
示例 1：

输入：nums = [3,7,1,6]
输出：5
解释：
一串最优操作是：
1. 选择 i = 1 ，nums 变为 [4,6,1,6] 。
2. 选择 i = 3 ，nums 变为 [4,6,2,5] 。
3. 选择 i = 1 ，nums 变为 [5,5,2,5] 。
nums 中最大值为 5 。无法得到比 5 更小的最大值。
所以我们返回 5 。
示例 2：

输入：nums = [10,1]
输出：10
解释：
最优解是不改动 nums ，10 是最大值，所以返回 10 。


提示：

n == nums.length
2 <= n <= 10^5
0 <= nums[i] <= 10^9


思考：
最小化最大值和最大化最小值，可以直接想到用二分答案的方法；
1. 做法就是找出二分的边界
2. 猜最大值，写一个check函数
这里的check函数就是要满足是最大值。
然后不断缩短右边边界来找到最小的最大值

left = 0
right = max(nums)



'''


from typing import List


def minimizeArrayValue(nums: List[int]) -> int:
    def check(limit):
        # 判断当前的limit，是不是调整改动之后的最大值
        a = nums.copy()
        # 从后往前不断的调整
        for i in range(len(nums) - 1, 0 , -1):
            x = a[i]
            if x > limit:
                a[i - 1] += x - limit
        return a[0] <= limit
    

    left, right = 0, max(nums)

    while left <= right:
        mid = (left + right) // 2
        if check(mid):  # 尝试找到更小的位置，向左找更小的位置
            right = mid - 1  # 收缩右边界
        else:
            left = mid + 1  # 增大左边界

    return left

print(minimizeArrayValue([3,7,1,6]))

        