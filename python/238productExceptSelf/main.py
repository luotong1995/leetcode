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


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    nums = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums))
