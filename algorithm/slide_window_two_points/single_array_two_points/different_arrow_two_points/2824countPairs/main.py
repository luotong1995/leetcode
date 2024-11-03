'''
2824. 统计和小于目标的下标数目

给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 target ，请你返回满足 0 <= i < j < n 且 nums[i] + nums[j] < target 的下标对 (i, j) 的数目。
 

示例 1：

输入：nums = [-1,1,2,3,1], target = 2
输出：3
解释：总共有 3 个下标对满足题目描述：
- (0, 1) ，0 < 1 且 nums[0] + nums[1] = 0 < target
- (0, 2) ，0 < 2 且 nums[0] + nums[2] = 1 < target 
- (0, 4) ，0 < 4 且 nums[0] + nums[4] = 0 < target
注意 (0, 3) 不计入答案因为 nums[0] + nums[3] 不是严格小于 target 。
示例 2：

输入：nums = [-6,2,5,-2,-7,-1,3], target = -2
输出：10
解释：总共有 10 个下标对满足题目描述：
- (0, 1) ，0 < 1 且 nums[0] + nums[1] = -4 < target
- (0, 3) ，0 < 3 且 nums[0] + nums[3] = -8 < target
- (0, 4) ，0 < 4 且 nums[0] + nums[4] = -13 < target
- (0, 5) ，0 < 5 且 nums[0] + nums[5] = -7 < target
- (0, 6) ，0 < 6 且 nums[0] + nums[6] = -3 < target
- (1, 4) ，1 < 4 且 nums[1] + nums[4] = -5 < target
- (3, 4) ，3 < 4 且 nums[3] + nums[4] = -9 < target
- (3, 5) ，3 < 5 且 nums[3] + nums[5] = -3 < target
- (4, 5) ，4 < 5 且 nums[4] + nums[5] = -8 < target
- (4, 6) ，4 < 6 且 nums[4] + nums[6] = -4 < target
 

提示：

1 <= nums.length == n <= 50
-50 <= nums[i], target <= 50

思考：

双指针：
求的是不重复的下标对的数量，所以排序不影响结果，可以使用双指针。
i=0
j=n-1
双指针，其实是迭代i，然后根据条件移动j，如果满足条件更新答案，不满足条件，更新j，此时需要注意的是，如果nums[i] + nums[j] >= target，则num[i+1] + nums[j] >= target一定成立，所以j的移动可以根据上一次的迭代继续。

二分查找
求的是不重复的下标对的数量，所以排序不影响结果，可以尝试使用二分查找
固定i则求j的取值范围：nums[j] < target - nums[i]，变成了二分查找求最大值
二分查找现在找到边界，left,right
'''


from bisect import bisect_left, bisect_right
from typing import List



def countPairs(nums: List[int], target: int) -> int:
    ans  = 0
    n = len(nums)
    for i in range(n - 1):
        for j in range(i+1, n):
            if nums[i] + nums[j] < target:
                ans += 1
    return ans

def countPairs2(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    ans  = 0
    j = n - 1
    for i in range(n - 1):
        while i < j:
            s = nums[i] + nums[j]
            if s >= target:
                j -= 1
            else:
                ans += j - i
                break

    return ans

def countPairs21(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    ans  = 0
    i = 0
    j = n - 1
    while i < j:
        s = nums[i] + nums[j]
        if s >= target:
            j -= 1
        else:
            ans += j - i
            i += 1
    return ans


def countPairs3(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    ans  = 0
    for i in range(n - 1):
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[i] + nums[mid] < target: #尝试找到更大的位置，尝试向右找更大的解
                left += 1
            else:
                right -= 1
                
        ans += right - i
    return ans

def countPairs4(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    ans  = 0
    for i in range(n - 1):
        left = i + 1
        right = n
        # 第一个大于等于target - nums[i]的位置的左边的位置即为我们找到的最后一个大于等于的位置
        ans += bisect_left(nums, target - nums[i], left, right) - 1  - i 
    return ans

# print(countPairs4([-1,1,2,3,1], 2))
# print(countPairs4([-6,2,5,-2,-7,-1,3], -2))
print(countPairs4([6,-1,7,4,2,3], 8))


print(bisect_left([-1,2,3,4,6,7], 9, 1,6))