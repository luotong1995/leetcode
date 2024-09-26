'''
给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。

同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。

请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。

 

示例 1：

输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7
输出：[4,0,3]
解释：
- 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。
- 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
- 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。
所以返回 [4,0,3] 。
示例 2：

输入：spells = [3,1,2], potions = [8,5,8], success = 16
输出：[2,0,2]
解释：
- 第 0 个咒语：3 * [8,5,8] = [24,15,24] 。总共 2 个成功组合。
- 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。
- 第 2 个咒语：2 * [8,5,8] = [16,10,16] 。总共 2 个成功组合。
所以返回 [2,0,2] 。
 

提示：

n == spells.length
m == potions.length
1 <= n, m <= 105
1 <= spells[i], potions[i] <= 105
1 <= success <= 1010

思考：
可以使用暴力求解，这里直接嵌套两层循环即可实现
这里直接使用二分查找，将时间复杂度降低,先找出大于等于success/item 的index，根据index，即可计算出数量,如果找不到，则返回的index为potions数组的长度，则没有符合条件的，返回0
'''


from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    def lower_bound(nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left  
    
    ans = []
    potions.sort()
    for item in spells:
        left_index = lower_bound(potions, success / item)
        if left_index == len(potions):
            ans.append(0)
        else:
            ans.append(len(potions) - left_index)
    return ans

spells = [3,1,2]
potions = [8,5,8]
success = 16
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs(spells, potions, success))
