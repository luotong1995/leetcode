'''
2958. 最多K个重复元素的最长子数组

给你一个整数数组 nums 和一个整数 k 。

一个元素 x 在数组中的 频率 指的是它在数组中的出现次数。

如果一个数组中所有元素的频率都 小于等于 k ，那么我们称这个数组是 好 数组。

请你返回 nums 中 最长好 子数组的长度。

子数组 指的是一个数组中一段连续非空的元素序列。

 

示例 1：

输入：nums = [1,2,3,1,2,3,1,2], k = 2
输出：6
解释：最长好子数组是 [1,2,3,1,2,3] ，值 1 ，2 和 3 在子数组中的频率都没有超过 k = 2 。[2,3,1,2,3,1] 和 [3,1,2,3,1,2] 也是好子数组。
最长好子数组的长度为 6 。
示例 2：

输入：nums = [1,2,1,2,1,2,1,2], k = 1
输出：2
解释：最长好子数组是 [1,2] ，值 1 和 2 在子数组中的频率都没有超过 k = 1 。[2,1] 也是好子数组。
最长好子数组的长度为 2 。
示例 3：

输入：nums = [5,5,5,5,5,5,5], k = 4
输出：4
解释：最长好子数组是 [5,5,5,5] ，值 5 在子数组中的频率没有超过 k = 4 。
最长好子数组的长度为 4 。
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length

思考：
求子数组的长度的问题，就是一个典型的Sliding Window问题，这里是一个变长的滑动窗口的问题；这里的条件是， LEFT 到 RIGHT 的所有元素的频率 <= k，然后这里可以用哈希表来实现，用python里面的counter来存储频率
1. left = 0
2. right = 0~n-1
3. 移动窗口的条件是：存在一个元素的频率>=k,这个freq[nums[right]]>=k,这里的freq用counter来实现
4. 更新ans=max(ans,right-left+1)

'''


from typing import Counter, List


def maxSubarrayLength(nums: List[int], k: int) -> int:
    left = 0
    ans = 0
    cnt = Counter()
    for right in range(len(nums)):
        while cnt[nums[right]] >= k:
            cnt[nums[left]] -= 1
            left += 1
        cnt[nums[right]] += 1
        ans = max(ans, right - left + 1)
    return ans

def maxSubarrayLength2(nums: List[int], k: int) -> int:
    left = 0
    ans = 0
    cnt = Counter()
    for right in range(len(nums)):
        cnt[nums[right]] += 1
        while cnt[nums[right]] > k:
            cnt[nums[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

print(maxSubarrayLength([1,2,1,2,1,2,1,2], 1))
print(maxSubarrayLength([1,2,1,2,1,2,1,2], 2))
print(maxSubarrayLength([5,5,5,5,5,5,5], 4))
print(maxSubarrayLength([1,1,1,2,2,2,3,3,3], 3))
print(maxSubarrayLength2([1,1,1,2,2,2,3,3,3], 3))