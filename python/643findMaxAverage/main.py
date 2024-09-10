'''
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

任何误差小于 10-5 的答案都将被视为正确答案。



示例 1：

输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
示例 2：

输入：nums = [5], k = 1
输出：5.00000


提示：

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    i = 0
    j = i + k
    n = len(nums)
    ans = sum(nums[i:j]) / k
    while j <= n:
        temp = sum(nums[i:j]) / k
        if ans <= temp:
            ans = temp
        i += 1
        j += 1
    return ans


def findMaxAverage2(nums: List[int], k: int) -> float:
    c_sum = sum(nums[0:k])
    max_sum = c_sum
    for i in range(k, len(nums)):
        c_sum = c_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, c_sum)
    return max_sum / k


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    # nums = [5]
    # k = 1
    # nums = [3, 3, 4, 3, 0]
    # k = 3
    # nums = [0, 1, 1, 3, 3]
    nums = [0, 4, 0, 3, 2]
    k = 1
    print(findMaxAverage2(nums, k))
