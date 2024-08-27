from typing import List


def longestConsecutive(nums: List) -> int:
    nums = sorted(list(set(nums)))
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    max_len = 1
    tmp = 1
    for i in range(1, len(nums)):
        if (nums[i] - nums[i - 1]) == 1:
            tmp += 1
        else:
            max_len = max(max_len, tmp)
            tmp = 1

    return max(max_len, tmp)


print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
