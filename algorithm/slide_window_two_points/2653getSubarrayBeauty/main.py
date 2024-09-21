'''
给你一个长度为 n 的整数数组 nums ，请你求出每个长度为 k 的子数组的 美丽值 。

一个子数组的 美丽值 定义为：如果子数组中第 x 小整数 是 负数 ，那么美丽值为第 x 小的数，否则美丽值为 0 。

请你返回一个包含 n - k + 1 个整数的数组，依次 表示数组中从第一个下标开始，每个长度为 k 的子数组的 美丽值 。

子数组指的是数组中一段连续 非空 的元素序列。

 

示例 1：

输入：nums = [1,-1,-3,-2,3], k = 3, x = 2
输出：[-1,-2,-2]
解释：总共有 3 个 k = 3 的子数组。
第一个子数组是 [1, -1, -3] ，第二小的数是负数 -1 。
第二个子数组是 [-1, -3, -2] ，第二小的数是负数 -2 。
第三个子数组是 [-3, -2, 3] ，第二小的数是负数 -2 。
示例 2：

输入：nums = [-1,-2,-3,-4,-5], k = 2, x = 2
输出：[-1,-2,-3,-4]
解释：总共有 4 个 k = 2 的子数组。
[-1, -2] 中第二小的数是负数 -1 。
[-2, -3] 中第二小的数是负数 -2 。
[-3, -4] 中第二小的数是负数 -3 。
[-4, -5] 中第二小的数是负数 -4 。
示例 3：

输入：nums = [-3,1,2,-3,0,-3], k = 2, x = 1
输出：[-3,0,-3,-3,-3]
解释：总共有 5 个 k = 2 的子数组。
[-3, 1] 中最小的数是负数 -3 。
[1, 2] 中最小的数不是负数，所以美丽值为 0 。
[2, -3] 中最小的数是负数 -3 。
[-3, 0] 中最小的数是负数 -3 。
[0, -3] 中最小的数是负数 -3 。
 

提示：

n == nums.length 
1 <= n <= 105
1 <= k <= n
1 <= x <= k 
-50 <= nums[i] <= 50 


思考：子数组的求法，需要使用滑动窗口，现在的问题如何求出第X小的数，由于nums的取值范围有限，所以使用暴力枚举
'''


from typing import List


def getSubarrayBeauty(nums: List[int], k: int, x: int) -> List[int]: 
    cnt = [0] * 101
    for num in nums[:k - 1]:  # 先往窗口内添加 k-1 个数
        cnt[num] += 1
    ans = [0] * (len(nums) - k + 1)
    for i, (in_, out) in enumerate(zip(nums[k - 1:], nums)):
        cnt[in_] += 1  # 进入窗口（保证窗口有恰好 k 个数）
        left = x
        for j in range(-50, 0):  # 暴力枚举负数范围 [-50,-1]
            left -= cnt[j]
            if left <= 0:  # 找到美丽值
                ans[i] = j
                break
        cnt[out] -= 1  # 离开窗口
    return ans

        
nums = [-3,1,2,-3,0,-3]
k = 2
x = 1
nums = [-1,-2,-3,-4,-5]
k = 2
x = 2
print(getSubarrayBeauty(nums, k, x))