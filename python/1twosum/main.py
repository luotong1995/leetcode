from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = i

    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in d and d[temp] != i:
            return [d[temp], i]
    return [-1, -1]
