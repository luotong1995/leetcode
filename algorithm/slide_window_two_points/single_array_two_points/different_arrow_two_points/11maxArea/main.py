'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。


输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水8和7之间，的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
 

提示：

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

思考：
这题需要求最大的面积，
然后面积等于，宽度乘高度低的元素。要想面积最大，所以要高度足够高并且宽度足够宽。
这个题目可以尝试使用双指针，left=0, right = n-1，此时area = n* min(nums[left], nums[right])。此时需要考虑如何移动指针；
想要面积更大，那要么高度变高，要么宽度变大，当前宽度最大了，所以只能够尝试把高度变高，尝试移动指针把高度变高；
此时要把高度低的指针进行移动，移动之后可能会出现高度变高，可能出现面积变大；但是如果把高度高的指针进行移动就会导致本身的高度和宽度都下降；

'''

from typing import List


def maxArea(height: List[int]) -> int:
    ans = 0
    i = 0
    j = len(height) - 1

    while i < j:
        ans = max(ans,(j-i) * min(height[i], height[j]))
        if height[i] <  height[j]:
            i += 1
        else:
            j -= 1
    return ans

print(maxArea([1,8,6,2,5,4,8,3,7]))