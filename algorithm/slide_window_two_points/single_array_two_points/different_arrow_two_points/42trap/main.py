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


这里使用前缀最大值，找出每个元素能够接的雨水的最高高度，然后通过前缀最大值和自身的高度的差，求出真实存放的水的容量。
所以这里先求出从左到右的前缀最大值，然后从右到左求出后缀最大值，即可求出当前数字的左边和右边的分别最高的，然后找出左右两边最大值的最小值即位水位高度，然后减去自身的高度，即为水的容量





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

def trap2(height: List[int]) -> int:
    # 求出每个元素的前缀最大值和后缀最大值
    # 前缀最大值即为元素前面的最大值和当前值比较的最大值
    # 后缀最大值即为元素后面的最大值和当前值比较的最大值

    ans = 0
    n = len(height)
    pre_max = [0]*n
    pre_max[0] = height[0]
    for i in range(1, n):
        pre_max[i] = max(pre_max[i-1], height[i])
    
    suf_max = [0]*n
    suf_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        suf_max[i] = max(suf_max[i+1], height[i])

    for i in range(n):
        ans += min(pre_max[i], suf_max[i]) - height[i]
    return ans


# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([4,2,0,3,2,5]))
print(trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
print(trap2([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
#                        1
#              1         1
# 1            1        11
# 1         1  11       11
# 11       11  11      111
# 11  1  1 111 111    1111 1
# 111 11 1 1111111  1 1111 1
# 111 11 111111111 111111111

# 64203203145327530121346813
        