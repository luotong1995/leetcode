'''
18.四数之和

给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

提示：

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9


[1,0,-1,0,-2,2]
[-2,-1,0,0,1,2] 0

直接套用三元组的方法来做，但是需要注意去除重复的方法，去除重复的方法同样也可以用set来做


'''


from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    ans = []
    nums.sort()
    n = len(nums)
    for i in range(n-3):
        # 跳过重复的数字
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            z = n - 1
            s = nums[i] + nums[j]+ nums[j+1]+ nums[j+2]
            if s > target:
                break
            s = nums[i] + nums[j]+ nums[-1]+ nums[-2]
            if s < target:
                continue

            while k < z:
                s = nums[i] + nums[j]+ nums[k]+ nums[z]
                if s > target:
                    z -= 1
                elif s < target:
                    k += 1
                else:
                    ans.append([nums[i], nums[j], nums[k], nums[z]])
                    k += 1
                    while k < z and nums[k] == nums[k - 1]:  # 跳过重复数字
                        k += 1
                    z -= 1
                    while z > k and nums[z] == nums[z + 1]:  # 跳过重复数字
                        z -= 1

    return ans


# print(fourSum([1,0,-1,0,-2,2], 0))
print(fourSum([2,2,2,2,2], 8))