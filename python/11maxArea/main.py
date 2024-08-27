from typing import List


# 暴力求解直接进行双循环，但是一定会超时，用双指针，要求面积最大，当然需要移动数值小的指针
def maxArea(height: List[int]) -> int:
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:

        if height[i] < height[j]:
            max_area = max(max_area, height[i] * (j - i))
            i += 1
        else:
            max_area = max(max_area, height[j] * (j - i))
            j -= 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
