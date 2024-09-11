'''
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序

进阶：
请你设计时间复杂度为 O(n) 的算法解决本问题
'''

from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    return sorted([item ** 2 for item in nums])


# 请你设计时间复杂度为 O(n) 的算法解决本问题
# 找到负数和正数，分别进行求解
# 然后进行归并排序
def sortedSquares2(nums: List[int]) -> List[int]:
    n = len(nums)
    neg_index = -1
    for i in range(n):
        if nums[i] < 0:
            neg_index = i
        else:
            break
    ans = []
    if neg_index == -1:
        ans = [item ** 2 for item in nums]
    elif neg_index == n - 1:
        ans = [item ** 2 for item in nums][::-1]
    else:
        i = neg_index + 1
        j = neg_index
        while i < n and j >= 0:
            if nums[i] ** 2 < nums[j] ** 2:
                ans.append(nums[i] ** 2)
                i += 1
            else:
                ans.append(nums[j] ** 2)
                j -= 1
        if i != n:
            ans.extend([item ** 2 for item in nums[i:]])
        if j != -1:
            ans.extend([item ** 2 for item in nums[:j + 1][::-1]])

    return ans


def merge_sort(arr):
    # 如果数组长度小于等于1，则直接返回
    if len(arr) <= 1:
        return arr

    # 找到数组的中间位置
    mid = len(arr) // 2

    # 递归地对左右两个子数组进行排序
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 合并已排序的子数组
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # 合并两个有序数组
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 将剩余的元素追加到结果数组中
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == '__main__':
    nums = [-7, -3, 2, 3, 11]
    nums = [-2, 0]
    print(sortedSquares2(nums))
