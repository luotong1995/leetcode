'''
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。


示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]


提示：

2 <= nums.length <= 105
-30 <= nums[i] <= 30
保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
'''

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    total_res = 1
    zero_num = 0
    for item in nums:
        if item != 0:
            total_res *= item
        else:
            zero_num += 1
    ans = []
    for item in nums:
        if item != 0:
            if zero_num:
                ans.append(0)
            else:
                ans.append(int(total_res / item))
        else:
            if zero_num > 1:
                ans.append(0)
            else:
                ans.append(total_res)
    return ans


## 前缀和后缀的方法
def productExceptSelf2(nums: List[int]) -> List[int]:
    length = len(nums)
    ans = [0] * length
    left = [0] * length
    right = [0] * length

    left[0] = 1
    for i in range(1, length):
        left[i] = nums[i - 1] * left[i - 1]

    right[length - 1] = 1
    for i in reversed(range(length - 1)):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(length):
        ans[i] = left[i] * right[i]

    return ans


# 用动态规划的思想来，不停的存储右边的元素
def productExceptSelf3(nums: List[int]) -> List[int]:
    length = len(nums)
    answer = [0] * length

    # answer[i] 表示索引 i 左侧所有元素的乘积
    # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    # R 为右侧所有元素的乘积
    # 刚开始右边没有元素，所以 R = 1
    R = 1
    for i in reversed(range(length)):
        # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
        answer[i] = answer[i] * R
        # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
        R *= nums[i]

    return answer

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    nums = [-1, 1, 0, -3, 3]
    print(productExceptSelf2(nums))
