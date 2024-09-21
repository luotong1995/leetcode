'''
给你一个整数数组 nums 和两个正整数 m 和 k 。

请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。

如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。

子数组指的是一个数组中一段连续 非空 的元素序列。


示例 1：

输入：nums = [2,6,7,3,1,7], m = 3, k = 4
输出：18
解释：总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7] 。这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。
示例 2：

输入：nums = [5,9,9,2,4,5,4], m = 1, k = 3
输出：23
解释：总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和 [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。
示例 3：

输入：nums = [1,2,1,2,1,2,1], m = 3, k = 3
输出：0
解释：输入数组中不存在长度为 k = 3 的子数组含有至少  m = 3 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。

思考：确实使用滑动窗口，但是如何确定几乎唯一，要求至少m个元素不相同,考虑使用哈希表来保证至少有m个不重复的元素


'''



from typing import List, Counter


def maxSum(nums: List[int], m: int, k: int) -> int:
    ans = 0
    cur_sum = 0
    n = len(nums)
    map = dict()
    for i in range(n):
        cur_sum += nums[i]
        map[nums[i]] = map.get(nums[i], 0) + 1
        if i < k - 1:
            continue
        
        
        if len(map) >= m:
            ans = max(ans,cur_sum)
        cur_sum = cur_sum - nums[i-k+1]
        if map.get(nums[i-k+1], 0) != 0:
            map[nums[i-k+1]] = map.get(nums[i-k+1], 0) - 1
        if map.get(nums[i-k+1], 0) == 0:
            map.pop(nums[i-k+1])
    return ans


def maxSum2(nums: List[int], m: int, k: int) -> int:
    ans = 0
    cur_sum = 0
    n = len(nums)
    cnt = Counter()
    for i in range(n):
        cur_sum += nums[i]
        cnt[nums[i]] += 1
        if i < k - 1:
            continue
        
        
        if len(cnt) >= m:
            ans = max(ans,cur_sum)
        cur_sum = cur_sum - nums[i-k+1]

        cnt[nums[i-k+1]] -= 1
        if cnt[nums[i-k+1]] == 0:
            del cnt[nums[i-k+1]]
    return ans



nums = [2,6,7,3,1,7]
m = 1
k = 4

nums = [1,2,1,2,1,2,1]
m = 3
k = 3


nums = [1,2,2]
m = 2
k = 2

print(maxSum2(nums, m, k))