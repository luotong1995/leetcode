'''
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

          1
1     1   1
1     1   1
1 1   1 1 1  1
1 1   1 1 1  1


              1
    1         1
    1     1   1
1   1 1   1 1 1
1   1 1   1 1 1

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9

思考：
可以使用双指针：
左右两端，找到第一个不是0的数字，然后求面积，
然后左边和右边分别移动，条件是左边往右移动需要移动到下一个更高的数字，同理右边往左边移动也需要移动到下一个更高的数字，然后再求面积。
知道left >= right


'''

from typing import List


def trap(height: List[int]) -> int:
    ans = 0
    left = 0
    right = len(height) - 1
    left_max = right_max = 0
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        if height[left] <= height[right]:
            ans += left_max - height[left]
            left += 1
        else:
            ans += right_max - height[right]
            right -= 1
    return ans

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([4,2,0,3,2,5]))
print(trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
#                        1
#              1         1
# 1            1        11
# 1         1  11       11
# 11       11  11      111
# 11  1  1 111 111    1111 1
# 111 11 1 1111111  1 1111 1
# 111 11 111111111 111111111

# 64203203145327530121346813
        