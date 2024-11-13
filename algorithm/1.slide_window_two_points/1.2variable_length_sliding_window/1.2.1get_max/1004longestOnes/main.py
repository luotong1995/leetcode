'''
1004. 最大连续1的个数III

给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。


示例 1：

输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 

提示：

1 <= nums.length <= 10^5
nums[i] 不是 0 就是 1
0 <= k <= nums.length

思考：
题目求的是最大的连续1的个数，可以用滑动窗口来求，在窗口中的0的个数不超过K即为合适的，当滑动窗口中的0的个数超过了k，移动左边端点
1. left=0
2. right=0~n-1
3. 统计滑动窗口的0的数量，如果0的数量大于k，则需要移动左边端口
4. 更新ans=max(right-left+1,ans)

'''



from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    zero_cnt = ans = left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_cnt += 1
            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
        ans = max(ans, right - left + 1)
    return ans

nums = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(longestOnes(nums, K))


