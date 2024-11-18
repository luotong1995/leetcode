'''
交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。

环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。

给你一个 二进制环形 数组 nums ，返回在 任意位置 将数组中的所有 1 聚集在一起需要的最少交换次数。

 

示例 1：

输入：nums = [0,1,0,1,1,0,0]
输出：1
解释：这里列出一些能够将所有 1 聚集在一起的方案：
[0,0,1,1,1,0,0] 交换 1 次。
[0,1,1,1,0,0,0] 交换 1 次。
[1,1,0,0,0,0,1] 交换 2 次（利用数组的环形特性）。
无法在交换 0 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 1 。
示例 2：

输入：nums = [0,1,1,1,0,0,1,1,0]
输出：2
解释：这里列出一些能够将所有 1 聚集在一起的方案：
[1,1,1,0,0,0,0,1,1] 交换 2 次（利用数组的环形特性）。
[1,1,1,1,1,0,0,0,0] 交换 2 次。
无法在交换 0 次或 1 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 2 。
示例 3：

输入：nums = [1,1,0,0,1]
输出：0
解释：得益于数组的环形特性，所有的 1 已经聚集在一起。
因此，需要的最少交换次数为 0 。
 

提示：

1 <= nums.length <= 10^5
nums[i] 为 0 或者 1

思考：先求出数字1的元素个数
然后根据这个长度来滑动窗口，统计0的个数，如果0的个数小于1的总数，则需要进行交换，不断的更新最小值；
对于环形结构，这里直接拼接字符串，将环形的元素拼接在数组的后面。

'''


import math
from typing import List


def minSwaps(nums: List[int]) -> int:
    n = len(nums)
    ans = math.inf
    total = sum(nums)
    cur_zero =0
    if total == 0:
        return 0

    for i in range(total):
        nums.append(nums[i])
    for i in range(n+total):
        if i < total - 1:
            if nums[i] == 0:
                cur_zero += 1
            continue
        
        if nums[i] == 0:
            cur_zero += 1
        ans = min(ans, cur_zero)

        if nums[i - total + 1] == 0:
            cur_zero -= 1

    return ans

print(minSwaps([0,1,0,1,1,0,0]))
print(minSwaps([0,1,1,1,0,0,1,1,0]))
print(minSwaps([1,1,0,0,1]))
print(minSwaps([0,0,0]))

