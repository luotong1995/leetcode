'''
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。


输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3


输入: nums = [4,2,3,4]
输出: 4

'''


# 先对数据进行排序，使用循环和二分查找的方法去找第三个数，看是否满足
# 用到的数学表达式为 a < b < c , a + b > c 则 a + c > b.则只需要判断 a + b > c 即可
def triangleNumber(nums):
    n = len(nums)
    nums.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            left, right, k = j + 1, n - 1, j
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < nums[i] + nums[j]:
                    k = mid
                    left = mid + 1
                else:
                    right = mid - 1
            ans += k - j
    return ans


if __name__ == '__main__':
    print(triangleNumber([2, 2, 3, 4]))
