'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]


提示:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''
from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    zero_count = sum([True if item == 0 else False for item in nums])

    for i in range(n - zero_count):
        if nums[i] == 0:
            j = i
            k = j + 1
            while k < n:
                if nums[k] != 0:
                    nums[j] = nums[k]
                    nums[k] = 0
                    j = k
                k += 1


# 快慢双指针
def moveZeroes2(nums: List[int]):
    n = len(nums)
    left = right = 0
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1


if __name__ == '__main__':
    a = [0, 1, 0, 3, 12]
    a = [0, 0, 1]
    moveZeroes(a)
    print(a)
