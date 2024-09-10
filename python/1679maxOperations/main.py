'''
给你一个整数数组 nums 和一个整数 k 。

每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。

返回你可以对数组执行的最大操作数。



示例 1：

输入：nums = [1,2,3,4], k = 5
输出：2
解释：开始时 nums = [1,2,3,4]：
- 移出 1 和 4 ，之后 nums = [2,3]
- 移出 2 和 3 ，之后 nums = []
不再有和为 5 的数对，因此最多执行 2 次操作。
示例 2：

输入：nums = [3,1,3,4,3], k = 6
输出：1
解释：开始时 nums = [3,1,3,4,3]：
- 移出前两个 3 ，之后nums = [1,4,3]
不再有和为 6 的数对，因此最多执行 1 次操作。

'''

from typing import List, Counter


def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    count = 0
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] > k:
            j -= 1
        elif nums[i] + nums[j] < k:
            i += 1
        else:
            count += 1
            i += 1
            j -= 1

    return count


def maxOperations2(nums: List[int], k: int) -> int:
    ans = 0
    cnt = Counter()
    for item in nums:
        if cnt[k - item]:
            cnt[k - item] -= 1
            ans += 1
        else:
            cnt[item] += 1
    return ans


if __name__ == '__main__':
    nums = [3, 1, 3, 4, 3]
    k = 6
    nums = [1, 2, 3, 4]
    k = 5
    print(maxOperations2(nums, k))
