'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。



思考：查找列表中是否存在target，存在返回相应的index，不存在返回-1
直接用>=的方式来进行二分查找，若存在直接返回index，不存在会存在三种情况，1. target大于nums中的最大值，2. target小于nums中的最小值，3. target在中间，但是不存在

>=的结果存在两种情况，1，找到了直接返回，2。没找到left到了数组长度的index 3. 返回了，但是left的值不等于target
'''


from typing import List


def search( nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == n or nums[left] != target:
        return -1
    return left

nums = [-1,0,3,5,9,12]
target = 2
print(search(nums, target))