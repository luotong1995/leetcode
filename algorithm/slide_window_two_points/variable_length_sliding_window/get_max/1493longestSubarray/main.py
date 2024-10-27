'''
1493. 删掉一个元素以后全为1的最长子数组

给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

 

提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
 

提示：

1 <= nums.length <= 10^5
nums[i] 要么是 0 要么是 1

思考：

首先这个题目有一个前提是必须要删除一个元素，所以如果不存在0则也会删除一个1.
这个题目也是可以用不定长滑动窗口来求解，条件就是窗口中的0的数量不能大于1即<=1


'''
from typing import List


def longestSubarray(nums: List[int]) -> int:
    left = 0
    zero_c = 0
    ans = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            while zero_c >= 1:
                if nums[left] == 0:
                    zero_c -= 1
                left += 1
            zero_c += 1

        ans = max(ans, right - left)
    return ans

def longestSubarray2(nums: List[int]) -> int:
    left = 0
    zero_c = 0
    ans = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_c += 1
            while zero_c > 1:
                if nums[left] == 0:
                    zero_c -= 1
                left += 1
        ans = max(ans, right - left)
    return ans

# nums = [1,1,0,1]
nums =  [0,1,1,1,0,1,1,0,1]
# nums = [1,1,1]
print(longestSubarray(nums))
print(longestSubarray2(nums))