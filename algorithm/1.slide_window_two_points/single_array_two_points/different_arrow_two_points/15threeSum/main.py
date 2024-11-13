'''

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 

提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 10^5

思考：
这题是twoSUM的扩展，对于三个数，可以先确定一个数，然后再通过双指针找两个数的和
这个题目是不会出现重复的三元组，所以可以对原序列进行排序，然后使用双指针
'''

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = set()
    for i in range(len(nums)- 2):
        x = nums[i]
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 这种情况，X还会变大，总和还有机会为0，所以continue
        if x + nums[-2] + nums[-1] < 0:
            continue
        # x已经跟最小的两个加和超过0了，所以之后的都不满足条件了
        if x + nums[i+1] + nums[i+2] > 0:
            break
        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = x + nums[j] + nums[k]
            if total == 0:
                # 需要拿到所有的，所以找到一个之后继续往后面找
                ans.add((x, nums[j], nums[k]))
                j += 1
                k -= 1
            elif total > 0:
                k -= 1
            else:
                j += 1
    return [list(item) for item in ans]



print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print(threeSum([-1,0,1,2,-1,-4]))