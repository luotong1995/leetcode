'''
使结果不超过阈值的最小除数

给你一个整数数组 nums 和一个正整数 threshold，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。

请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。

每个数除以除数后都向上取整，比方说 7/3 = 3，10/2 = 5 。

题目保证一定有解。

 

示例 1：

输入：nums = [1,2,5,9], threshold = 6
输出：5
解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
示例 2：

输入：nums = [2,3,5,7,11], threshold = 11
输出：3
示例 3：

输入：nums = [19], threshold = 5
输出：4
 

提示：

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6

思考：
首先需要找到相应的临界值，比如取数组中的最大值，肯定有解，和为数组的长度n。
但是这个值很大，需要从1-最大的值之间，找到最小的这个值，满足条件。使用二分查找的方法来查找，第一个满足条件的值，sum([item / x for item in nums]) <= threshold。
还是用lowerbound的思路，求出第一个满足条件的数

'''

from typing import List
from bisect import bisect_right, bisect_left




def binary_search_min(nums, threshold, cands):
    def get_x(a, b):
        return a//b + (1 if a%b else 0)

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if sum([get_x(item, nums[mid]) for item in cands]) <= threshold:
            right = mid - 1
        else:
            left = mid + 1

    return nums[left]


def smallestDivisor(nums: List[int], threshold: int) -> int:
    max_value = max(nums)
    min_value = 1
    return binary_search_min([item for item in range(min_value, max_value + 1)], threshold, nums)

nums = [2,3,5,7,11]
threshold = 11

# nums = [1,2,5,9]
# threshold = 6

# nums = [19]
# threshold = 5
print(smallestDivisor(nums, threshold))