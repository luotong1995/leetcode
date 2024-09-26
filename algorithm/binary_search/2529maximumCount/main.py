'''
给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。

换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
注意：0 既不是正整数也不是负整数。

 

示例 1：

输入：nums = [-2,-1,-1,1,2,3]
输出：3
解释：共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
示例 2：

输入：nums = [-3,-2,-1,0,0,1,2]
输出：3
解释：共有 2 个正整数和 3 个负整数。计数得到的最大值是 3 。
示例 3：

输入：nums = [5,20,66,1314]
输出：4
解释：共有 4 个正整数和 0 个负整数。计数得到的最大值是 4 。
 

提示：

1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums 按 非递减顺序 排列。
 

进阶：你可以设计并实现时间复杂度为 O(log(n)) 的算法解决此问题吗？

思考：
1. 可以使用最简单的方法，然后判断元素是否的符号，时间复杂度是O(n)
2. 使用二分查找的方法，找出第一个大于等于0的位置，然后找出最后一个小于等于0的位置，根据下标和数组的长度即可计算，正整数的数量和负整数的数量

'''



from typing import List


def maximumCount(nums: List[int]) -> int:
    def lower_bound(nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    length = len(nums)
    left_index = lower_bound(nums, 0)
    # if left_index == len(nums) or nums[left_index] != 0:
        # left_index = -1
        # return length
        
    right_index = lower_bound(nums, 1) - 1 
    # if right_index == len(nums) or nums[right_index] != 0:
        # right_index = -1
        # return length
    
    
    return max(left_index, length - 1 - right_index)


nums = [-2,-1,-1,1,2,3]
nums = [-2,-1,-1]
print(maximumCount(nums))