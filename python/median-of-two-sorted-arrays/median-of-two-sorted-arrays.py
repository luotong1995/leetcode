from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    l = len(nums1) + len(nums2)
    nums1 = nums1 + nums2
    nums1.sort()
    if l % 2:
        return nums1[l // 2]
    else:
        a = l // 2
        return (nums1[a - 1] + nums1[a]) / 2


if __name__ == '__main__':
    print(findMedianSortedArrays([1, 3], [3, 4]))
