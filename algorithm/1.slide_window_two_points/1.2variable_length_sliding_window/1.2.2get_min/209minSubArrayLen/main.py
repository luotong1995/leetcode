'''
209. 长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 
子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
 

提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

思考：
求的还是子数组的长度，与求最大的区别是求最小，条件是和总是大于等于 target
然后判断当前和 - nums[left] 是否大于target,如果大于等于target不断的将left向右移动，不断的缩小空间，用来求最小。
这样就能求到right的下标的最小值。


'''


from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0 
    ans = len(nums) + 1
    cnt = 0
    for right in range(len(nums)):
        cnt += nums[right]
        while cnt - nums[left] >= target:
            cnt -= nums[left]
            left += 1
        if cnt >= target:
            ans = min(ans, right - left + 1)
    return ans if ans <= len(nums) else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))

        