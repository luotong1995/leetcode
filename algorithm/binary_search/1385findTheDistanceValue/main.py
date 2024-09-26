'''
给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。

「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。

 

示例 1：

输入：arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
输出：2
解释：
对于 arr1[0]=4 我们有：
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
所以 arr1[0]=4 符合距离要求

对于 arr1[1]=5 我们有：
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
所以 arr1[1]=5 也符合距离要求

对于 arr1[2]=8 我们有：
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
存在距离小于等于 2 的情况，不符合距离要求 

故而只有 arr1[0]=4 和 arr1[1]=5 两个符合距离要求，距离值为 2
示例 2：

输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
输出：2
示例 3：

输入：arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
输出：1
 

提示：

1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100

思考：
暴力求解，直接两层嵌套循环求解,能过，但是很慢。
考虑别的方法实现，二分查找，对于arr2进行排序，判断是否符合要求，如果出现不符合要求即|x-y| <= d，排序之后，找到第一个大于等于x的数和小于x的最大的y的数，即第一个大于等于x的数的前面的那个数，如果满足|x-y| <= d条件，则跳过，反之满足题目要求。
'''

from typing import List


def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    ans = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if abs(arr1[i] - arr2[j]) <= d:
                break
            if j == len(arr2) - 1:
                ans += 1
    return ans



def findTheDistanceValue2(arr1: List[int], arr2: List[int], d: int) -> int:
    ans = 0
    def lower_bound(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                # [mid + 1, right]
                left = mid + 1
            else:
                right = mid - 1
        return left
    arr2.sort()
    for item in arr1:
        ok = True
        left_index = lower_bound(arr2, item)
        if left_index < len(arr2) and abs(item- arr2[left_index]) <= d:
            ok = False
            continue
        if left_index - 1 >= 0 and abs(item-arr2[left_index - 1]) <= d:
            ok = False
            continue
        if ok:
            ans += 1

    return ans

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(findTheDistanceValue2(arr1, arr2, d))
