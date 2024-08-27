from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    a1 = set(nums1)
    a2 = set(nums2)
    for item in nums2:
        if item in a1:
            a1.remove(item)
    for item in nums1:
        if item in a2:
            a2.remove(item)
    return [list(a1), list(a2)]


print(findDifference([1, 2, 3], [2, 4, 6]))
