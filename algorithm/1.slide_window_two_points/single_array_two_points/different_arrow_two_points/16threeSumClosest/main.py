'''
16.最接近的三数之和

给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

 

示例 1：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
示例 2：

输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
 

提示：

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4


思考：
[-4,-1,1,2], 1
固定第一个数，然后使用双指针找到此时这种情况下最接近的组合，如何最接近即（x + y + z - target）最接近0
while j < k 
 找到最接近的组合
 

类似，排序后，枚举 nums[i] 作为第一个数，那么问题变成找到另外两个数，使得这三个数的和与 target 最接近，这同样可以用双指针解决。

设 s=nums[i]+nums[j]+nums[k]，为了判断 s 是不是与 target 最近的数，我们还需要用一个变量 minDiff 维护 ∣s−target∣ 的最小值。分类讨论：

如果 s=target，那么答案就是 s，直接返回 s。
如果 s>target，那么如果 s−target<minDiff，说明找到了一个与 target 更近的数，更新 minDiff 为 s−target，更新答案为 s。然后和三数之和一样，把 k 减一。
否则 s<target，那么如果 target−s<minDiff，说明找到了一个与 target 更近的数，更新 minDiff 为 target−s，更新答案为 s。然后和三数之和一样，把 j 加一。
除此以外，还有以下几个优化：

设 s=nums[i]+nums[i+1]+nums[i+2]。如果 s>target，由于数组已经排序，后面无论怎么选，选出的三个数的和不会比 s 还小，所以不会找到比 s 更优的答案了。所以只要 s>target，就可以直接 break 外层循环了。在 break 前判断 s 是否离 target 更近，如果更近，那么更新答案为 s。

设 s=nums[i]+nums[n−2]+nums[n−1]。如果 s<target，由于数组已经排序，nums[i] 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了，无法找到比 s 更优的答案。但是后面还有更大的 nums[i]，可能找到一个离 target 更近的三数之和，所以还需要继续枚举，continue 外层循环。在 continue 前判断 s 是否离 target 更近，如果更近，那么更新答案为 s，更新 minDiff 为 target−s。


'''


from math import inf
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    ans = 0
    nums.sort()
    n = len(nums)
    gap = inf
    for i in range(n-2):
        j = i + 1
        k = n - 1
        s = nums[i] + nums[i+ 1] + nums[i+2]
        if s > target:
            if s - target < gap:
                gap = s - target
                ans = s
                break
        s = nums[i] + nums[-1] + nums[-2]
        if s < target:
            if target - s > gap:
                gap = target -s 
                ans = s
                continue

        while j < k:
            s = nums[i] + nums[j] + nums[k]
            
            if s - target < 0:
                if target - s < gap:
                    ans = s
                    gap = target - s
                j += 1
            elif s - target >0:
                if s - target < gap:
                    ans = s
                    gap = s - target
                k -= 1
            else:
                ans = s
                break
    return ans

# print(threeSumClosest([-1,2,1,-4], 1))
# print(threeSumClosest( [0,0,0], 1))
print(threeSumClosest( [1,1,1,0], -100))
    