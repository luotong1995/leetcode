'''
1658. 将x减到0的最小操作数

给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

 

示例 1：

输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
示例 2：

输入：nums = [5,6,7,8,9], x = 4
输出：-1
示例 3：

输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9

思考：
顺着题目思考，很难想到方法，可以使用逆向思维，要找到最小的操作数量，而且操作的都是最外层，所以直接用滑动窗口来找到剩下的数字和为sum(nums) - x的，然后求出最大的滑动窗口的数字和为sum(nums) -x;

即为：最小的操作数量，最小操作数量等于len(nums) - 最大滑动窗口的元素个数


'''


from typing import List


def minOperations(nums: List[int], x: int) -> int:
    left = cnt = 0
    ans = -1
    total = sum(nums)
    if total < x:
        return -1
    for right in range(len(nums)):
        cnt += nums[right]
        while cnt > total - x:
            cnt -= nums[left]
            left += 1
        if cnt == total - x:
            ans = max(ans, right - left + 1)
    if ans == -1:
        return -1
    return len(nums) - ans

nums = [1,1,4,2,3]
x = 5
nums = [5,6,7,8,9]
x = 4

nums = [3,2,20,1,1,3]
x = 10
nums = [1,1]
x = 3
nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
x = 134365
print(minOperations(nums, x))