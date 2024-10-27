'''
1695. 删除子数组的最大最大得分

给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。

返回 只删除一个 子数组可获得的 最大得分 。

如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

 

示例 1：

输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
示例 2：

输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

思考：
本题目求的是子数组中的元素和最大且子数组中不含重复元素，所以最终的结果是求的和最大。即可使用可变长的滑动窗口来实现。让滑动窗口中出现重复的元素的时候，移动窗口左边的端点。
1. left = 0
2. right = 0~n-1
3. 使用一个set()来存储当前widnow中元素，当right的元素在set()中存在，left++，直到没有重复的元素为止
4. 更新ans=max(ans,sum(nums[left:right+1]))

'''

from typing import List


def maximumUniqueSubarray(nums: List[int]) -> int:
    left = 0
    ans = 0
    window =set()
    count = 0
    for right in range(len(nums)):
        while nums[right] in window:
            window.remove(nums[left])
            count -= nums[left]
            left += 1
        window.add(nums[right])
        count += nums[right]
        ans = max(ans,count)
    return ans

nums = [4,2,4,5,6]
print(maximumUniqueSubarray(nums))
