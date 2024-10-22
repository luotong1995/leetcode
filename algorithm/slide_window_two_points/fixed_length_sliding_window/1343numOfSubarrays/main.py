'''
给你一个整数数组 arr 和两个整数 k 和 threshold 。

请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

 

示例 1：

输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
示例 2：

输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
 

提示：

1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
'''

from typing import List


def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    ans = 0
    c_sum = 0
    for i in range(len(arr)):
        c_sum += arr[i]

        if i < k -1:
            continue
        if c_sum / k >= threshold:
            ans += 1
        
        c_sum -= arr[i-k+1]
    return ans

arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(numOfSubarrays(arr, k, threshold))
        

