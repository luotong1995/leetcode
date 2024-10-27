'''
2962. 统计最大元素出现至少K次的子数组

给你一个整数数组 nums 和一个 正整数 k 。

请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。

子数组是数组中的一个连续元素序列。

 

示例 1：

输入：nums = [1,3,2,3,3], k = 2
输出：6
解释：包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3] 。
示例 2：

输入：nums = [1,4,2,1], k = 3
输出：0
解释：没有子数组包含元素 4 至少 3 次。
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5

思考：

方法1:
1. 先求出最大值max(nums)
2. 固定左端点，求出每个左端点满足的结果
3. 如果nums[right] = max_data, cnt +=1 
4. 如果cnt>=k, 则ans += n - right，如果nums[left] == max_data: cnt -= 1，移动left ++；直到cnt < k


固定左端点，然后开始查找的过程，所以我们只需要每次都找到一个符合条件的子串，那么后面的所有附加的子串都会符合条件.
所以这个题目的每一个left都可以求满足条件的结果

这里我们以题目中的[1, 3, 2, 3, 3]为例子。 当我们第一次往右拓展窗口的时候，达到了[1, 3, 2, 3]这样一个子串，已经满足最大值的个数超过两个了，
那么后续的添加任意数字也必定是符合条件，所以我们找到这个符合条件的小窗口之后，后续的[1, 3, 2, 3, 3]也必定是符合条件的，所以我们需要ans += n - right，
然后继续移动left。
移动left的条件就是最大元素的次数>=k


方法2:
1. 设 mx=max(nums)。
2. 右端点 right 从左到右遍历 nums。遍历到元素 x=nums[right] 时，如果 x=mx，就把计数器 cntMx 加一。
3. 如果此时 cntMx=k，则不断右移左指针 left，直到窗口内的 mx 的出现次数小于 k 为止。此时，对于右端点为 right 且左端点小于 left 的子数组，mx的出现次数都至少为k，把答案增加 left。

'''


from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
    cnt = ans = left = 0
    mx = max(nums)
    n = len(nums)
    for right in range(len(nums)):
        if nums[right] == mx:
            cnt += 1
        while cnt >= k:
            ans += (n - right)
            if nums[left] == mx:
                cnt -= 1
            left += 1
    return ans

def countSubarrays2(nums: List[int], k: int) -> int:
    cnt = ans = left = 0
    mx = max(nums)
    for right in range(len(nums)):
        if nums[right] == mx:
            cnt += 1
        while cnt >= k:
            if nums[left] == mx:
                cnt -= 1
            left += 1
        ans += left
    return ans


print(countSubarrays2([1, 3, 2, 3, 3], 2))
        