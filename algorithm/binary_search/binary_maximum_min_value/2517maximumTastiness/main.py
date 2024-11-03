'''
2517. 礼盒最大甜蜜度

给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。

商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。

返回礼盒的 最大 甜蜜度。

 

示例 1：

输入：price = [13,5,1,8,21,2], k = 3
输出：8
解释：选出价格分别为 [13,5,21] 的三类糖果。
礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
可以证明能够取得的最大甜蜜度就是 8 。
示例 2：

输入：price = [1,3,1], k = 2
输出：2
解释：选出价格分别为 [1,3] 的两类糖果。 
礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
可以证明能够取得的最大甜蜜度就是 2 。
示例 3：

输入：price = [7,7,7,7], k = 2
输出：0
解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。
 

提示：

2 <= k <= price.length <= 10^5
1 <= price[i] <= 10^9

思考：
这个题目是最大化最小值，所以典型的使用二分答案的方法来做
1. left=0, right=max(nums) - min(nums)
2. nums.sort() 排序对当前题目结果无影响；
3. 写check函数                                                            
单调性如何找，甜蜜度越大，找到K个类的难度更大，甜蜜度越小，找到K个类越容易
假设x为给定的甜蜜度，从nums从小到大找，如果存在K个这样的组合，则说明小于x的数字也满足，
如果找不到这样的k种糖果，则说明大于x的也不满足，即存在单调性。

这个题目在更新二分边界的时候，会发现数字越小越成立，所以是一个求最大的情况，越小越满足，越大越不满足

[13,5,1,8,21,2]
[1,2,5,8,13,21]

猜测x=7
从第一个元素开始找
[1,8,21]  满足，那肯定x<7也满足

猜测x=9
从第一个元素开始找
[1,13]  只有两个不满足满足，那肯定x>9也不满足

'''


from typing import List


def maximumTastiness(price: List[int], k: int) -> int:
    # 满足要求
    def check(x):
        cnt = 1
        x0 = price[0]
        for item in price:
            if item>= x + x0:
            # item可以选
                cnt += 1
                x0 = item
        return cnt >= k
    
    price.sort()
    left = 0
    right = price[-1] - price[0]
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

# print(maximumTastiness([1,3,1], 2))
print(maximumTastiness([13,5,1,8,21,2], 3))