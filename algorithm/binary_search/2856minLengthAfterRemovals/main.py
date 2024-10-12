'''
给你一个下标从 0 开始的 非递减 整数数组 nums 。

你可以执行以下操作任意次：

选择 两个下标 i 和 j ，满足 nums[i] < nums[j] 。
将 nums 中下标在 i 和 j 处的元素删除。剩余元素按照原来的顺序组成新的数组，下标也重新从 0 开始编号。
请你返回一个整数，表示执行以上操作任意次后（可以执行 0 次），nums 数组的 最小 数组长度。


示例 1：

输入：nums = [1,2,3,4]

输出：0

解释：



示例 2：

输入：nums = [1,1,2,2,3,3]

输出：0

解释：



示例 3：

输入：nums = [1000000000,1000000000]

输出：2

解释：

由于两个数字相等，不能删除它们。

示例 4：

输入：nums = [2,3,4,4,4]

输出：1

解释：

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
nums 是 非递减 数组。

思考：
如果求最大的数的数量maxCnt，如果maxCnt大于数组长度n的一半，则最后剩下的数量为maxCnt - n/2
如果maxCnt*2 <=n 且为n为偶数，可以将除了最大的数以外的所有的数消除的只剩maxCnt个，最后再与最大的数进行消除，最终剩下0
如果maxCnt*2 <=n 且n为奇数，同上，最后剩下1个数

求maxCnt
'''

from typing import List
from collections import OrderedDict


def minLengthAfterRemovals(nums: List[int]) -> int:
    n = len(nums)
    sorted_dict = OrderedDict()
    for item in nums:
        if item not in sorted_dict:
            sorted_dict[item] = 1
        else:
            sorted_dict[item] += 1
    sorted_dict = dict(sorted(sorted_dict.items(), key=lambda x: x[1]))
    max_key, maxCnt = list(sorted_dict.items())[-1]
    if maxCnt * 2 <=n:
        if n % 2:
            return 1
        else:
            return 0
    else:
        return maxCnt * 2 -n

nums = [2,3,4,4,4]
nums = [1,1,1,1,1,1,1,2,2]
# nums = [1,2,3,4]
print(minLengthAfterRemovals(nums))

