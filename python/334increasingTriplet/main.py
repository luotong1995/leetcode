'''
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

示例 1：

输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
示例 2：

输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组
示例 3：

输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6


提示：
子序列是可以不连续的

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
'''
from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    a = float('inf')
    b = float('inf')
    for item in nums:
        if item <= a:
            a = item
        elif item <= b:
            b = item
        else:
            return True
    return False


# 递增子序列，对于每个元素，在左边存在元素小于当前元素，在右边存在元素大于当前元素
# 所以用两个list来存储结果，一个存储左边的最小值，一个存储右边的最大值
def increasingTriplet2(nums: List[int]) -> bool:
    l = [0] * len(nums)
    r = [0] * len(nums)
    l[0] = nums[0]
    for i in range(1, len(nums)):
        l[i] = min(l[i - 1], nums[i])

    r[len(r) - 1] = nums[len(nums) - 1]
    for i in range(len(nums) - 2, -1, -1):
        r[i] = max(r[i + 1], nums[i])

    for i in range(1, len(nums) - 1):
        if l[i] < nums[i] < r[i]:
            return True
    return False


if __name__ == '__main__':
    print(increasingTriplet([20, 100, 10, 12, 5, 13]))
    print(increasingTriplet([2, 1, 5, 0, 4, 6]))
    print(increasingTriplet2([20, 100, 10, 12, 5, 13]))
    print(increasingTriplet2([2, 1, 5, 0, 4, 6]))
