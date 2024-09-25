'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109


### 解题思路：二分查找lower_bound 【时间复杂度O(lgn),n是数组长度】

- 核心要素
- 注意区间开闭，三种都可以
- 循环结束条件：当前区间内没有元素
- 下一次二分查找区间：不能再查找(区间不包含)mid，防止死循环
- 返回值：大于等于target的第一个下标（注意循环不变量）

- 有序数组中二分查找的四种类型（下面的转换仅适用于数组中都是整数）
1. 第一个大于等于x的下标： low_bound(x)
2. 第一个大于x的下标：可以转换为`第一个大于等于 x+1 的下标` ，low_bound(x+1)
3. 最后一个一个小于x的下标：可以转换为`第一个大于等于 x 的下标` 的`左边位置`, low_bound(x) - 1;
4. 最后一个小于等于x的下标：可以转换为`第一个大于等于 x+1 的下标` 的 `左边位置`, low_bound(x+1) - 1;

'''


from typing import List

def lower_abound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            # [mid + 1, right]
            left = mid + 1
        else:
            right = mid - 1
    return left



def searchRange(nums: List[int], target: int) -> List[int]:
    # >= target
    start = lower_abound(nums, target)
    if start == len(nums) or nums[start] != target:
        return [-1,-1]
    # <= target
    end = lower_abound(nums, target + 1) - 1
    return [start, end]
 

nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums, target))