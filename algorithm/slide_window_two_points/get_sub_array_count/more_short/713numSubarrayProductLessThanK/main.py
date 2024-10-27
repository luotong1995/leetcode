'''

给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
 

示例 1：

输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
示例 2：

输入：nums = [1,2,3], k = 0
输出：0
 

提示: 

1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6

思考：
先用滑动窗口求出以right为右端点的满足条件的最长的子数组；[10,5]就是一个以5为右端点的最长的子数组. 
然后求出总共的子数组的个数


'''

from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    ans = 0
    left = 0
    prod = 1
    if k <= 1:
        return 0
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k :
            prod /= nums[left]
            left += 1
        ans += (right - left + 1)
    return ans

print(numSubarrayProductLessThanK([10,5,2,6], 0))
