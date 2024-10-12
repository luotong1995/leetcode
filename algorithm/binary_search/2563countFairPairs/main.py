'''
统计公平数对的数目

给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。

如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：

0 <= i < j < n，且
lower <= nums[i] + nums[j] <= upper
 

示例 1：

输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6
输出：6
解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
示例 2：

输入：nums = [1,7,9,2,5], lower = 11, upper = 11
输出：1
解释：只有单个公平数对：(2,3) 。


思考：
1. 直接暴力求解, 本题过不了，会超时
2. 直接排序，找出正确的对的个数就好，不需要确定具体的对子，所以先排序，然后枚举nums[j],然后用二分查找的方法去找nums[i]
lower - nums[j] <= nums[i] <= upper - nums[j]

'''

from bisect import bisect_right, bisect_left
from typing import List


def countFairPairs( nums: List[int], lower: int, upper: int) -> int:
    n = len(nums)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] >= lower and nums[i] + nums[j] <= upper:
                ans += 1
    return ans            
    
def lower_bound(nums, target):
    n = len(nums)
    l = 0
    r = n -1 
    while l <= r:
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

def countFairPairs2( nums: List[int], lower: int, upper: int) -> int:
    n = len(nums)
    ans = 0
    nums.sort()
    for j,item in enumerate(nums):
        if item > upper:
            continue
        c_nums = nums[:j]
        n = len(c_nums)
        left = lower_bound(c_nums, lower - item)
        right = lower_bound(c_nums, upper - item + 1) - 1

        ans += right - left + 1
    return ans            
    



nums = [1,7,9,2,5]
lower = 11
upper = 11

nums = [0,0,0,0,0,0]
lower = 0
upper = 0
print(countFairPairs2(nums, lower, upper))