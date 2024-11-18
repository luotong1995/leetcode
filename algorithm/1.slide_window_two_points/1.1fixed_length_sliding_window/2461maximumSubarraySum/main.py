'''
给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：

子数组的长度是 k，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。

子数组 是数组中一段连续非空的元素序列。

 

示例 1：

输入：nums = [1,5,4,2,9,9,9], k = 3
输出：15
解释：nums 中长度为 3 的子数组是：
- [1,5,4] 满足全部条件，和为 10 。
- [5,4,2] 满足全部条件，和为 11 。
- [4,2,9] 满足全部条件，和为 15 。
- [2,9,9] 不满足全部条件，因为元素 9 出现重复。
- [9,9,9] 不满足全部条件，因为元素 9 出现重复。
因为 15 是满足全部条件的所有子数组中的最大子数组和，所以返回 15 。
示例 2：

输入：nums = [4,4,4], k = 3
输出：0
解释：nums 中长度为 3 的子数组是：
- [4,4,4] 不满足全部条件，因为元素 4 出现重复。
因为不存在满足全部条件的子数组，所以返回 0 。
'''

from typing import List, Counter


def maximumSubarraySum( nums: List[int], k: int) -> int:
    ans = 0
    cur_sum = 0
    n = len(nums)
    map = dict()
    for i in range(n):
        cur_sum += nums[i]
        map[nums[i]] = map.get(nums[i], 0) + 1
        if i < k - 1:
            continue
        
        
        if len(map) == k:
            ans = max(ans,cur_sum)
        cur_sum = cur_sum - nums[i-k+1]
        if map.get(nums[i-k+1], 0) != 0:
            map[nums[i-k+1]] = map.get(nums[i-k+1], 0) - 1
        if map.get(nums[i-k+1], 0) == 0:
            map.pop(nums[i-k+1])
    return ans

nums = [1,5,4,2,9,9,9]
k = 3

nums = [4,4,4]
k = 3
print(maximumSubarraySum(nums, k))