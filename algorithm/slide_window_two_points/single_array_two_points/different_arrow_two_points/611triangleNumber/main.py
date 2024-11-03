'''
611.有效的三角形个数

给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
 
示例 1:

输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
示例 2:

输入: nums = [4,2,3,4]
输出: 4
[2,3,4]
[2,3,4]
[2,4,4]
[3,4,4]
 

提示:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000

思考：
三数之和的方法来做

首先明确计算规则：从示例 1 可以知道，对于三元组 (2,3,4) 和 (4,3,2)，我们只统计了其中的 (2,3,4)，并没有把 (4,3,2) 也统计到答案中，所以题目意思是把这两个三元组当成是同一个三元组，我们不能重复统计。

既然有这样的规则，那么不妨规定三角形的三条边 a,b,c 满足：

1≤a≤b≤c
这可以保证我们在统计合法三元组 (a,b,c) 的个数时，不会把 (c,b,a) 这样的三元组也统计进去。

由于三角形两边之和大于第三边，我们有

a+b>c
a+c>b
b+c>a

上式中的 a+c>b 是必然成立的，因为 a+c≥a+b>b（注意 a 至少是 1）。

同样的，b+c>a 也必然成立，因为 b+c≥a+a=2a>a（注意 a 至少是 1）。

所以只需要考虑第一个式子，那么问题变成，从 nums 中选三个数，满足 1≤a≤b≤c 且 a+b>c 的方案数。

1≤a≤b≤c


'''

from typing import List


def triangleNumber(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    ans = 0
    for i in range(2, n):
        j = 0 
        k = i - 1
        while j < k:
            if nums[j] + nums[k] <= nums[i]:
                j += 1
            else:
                # 从j到k的组合都满足
                ans += k - j
                k -= 1
    return ans



print(triangleNumber([2,2,3,4]))
print(triangleNumber([4,2,3,4]))
        