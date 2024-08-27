from typing import List


# 单调栈，求下一个更大的元素
def nextGreaterElement(nums1: List[int]) -> List[int]:
    result = [-1] * len(nums1)
    stack = []
    for i in range(len(nums1)):
        while stack and nums1[i] > nums1[stack[-1]]:
            result[stack[-1]] = nums1[i]
            stack.pop()
        stack.append(i)

    return result


def nextGreaterElement2(nums1: List[int], nums2: List[int]):
    stack = []
    a_dict = {}
    res = [0] * len(nums1)
    for i in range(len(nums2)):
        while stack and nums2[i] > stack[-1]:
            a_dict[stack[-1]] = nums2[i]
            stack.pop()
        stack.append(nums2[i])

    for i in range(len(nums1)):
        res[i] = a_dict.get(nums1[i], -1)
    return res


print(nextGreaterElement2([1, 2], [1, 2, 3, 5, 4, 7]))
