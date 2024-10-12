'''
# 区间内查询数字的频率

请你设计一个数据结构，它能求出给定子数组内一个给定值的频率。

子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。

请你实现 RangeFreqQuery 类：

RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。
一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。

 

示例 1：

输入：
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
输出：
[null, 1, 2]

解释：
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。
 

思考：
首先，RangeFreQuery使用来初始化的，将给定的数组值初始化；
query，用来查询，最简单的是想到，直接循环一次数组进行找，统计出现的次数；
进阶一点：排序之后使用二分查找，使用hash表存储已经查询过的结果，如果再次出现，直接返回
上面这种方法会出现超时的情况；

再次思考：
先找出value所有的index，存储起来，这样存储的都是值为value的下标的有序数组；
然后再用left和right，使用二分查找的方法在下标的有序数组找出，第一个大于等于left的数组下标l，和第一个大于等于right + 1的数组下标r。
结果就是r - l


'''

from collections import defaultdict
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.result = {}
        self.distinct = set(arr)

    def lower_bound(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def query(self, left: int, right: int, value: int) -> int:
        if len(self.distinct) == 1 and value in self.distinct:
            return right - left + 1
        k = str(left) + ':' + str(right) + ':' + str(value)
        if k in self.result:
            return self.result[k]

        arr = self.arr[left:right+1]
        arr.sort()
        l_index = self.lower_bound(arr, value)
        if  l_index == len(arr) or arr[l_index] != value:
            self.result[k] = 0
            return 0
            
        r_index = self.lower_bound(arr, value + 1)
        
        self.result[k] = r_index - l_index
        return r_index - l_index


class RangeFreqQuery2:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.index_order = defaultdict(list)
        for i in range(len(arr)):
            self.index_order[arr[i]].append(i)

        

    def lower_bound(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def query(self, left: int, right: int, value: int) -> int:
        pos_array = self.index_order[value]
        l_index = self.lower_bound(pos_array, left)
        r_index = self.lower_bound(pos_array, right + 1)
        return r_index - l_index



arr = [1,1,1]


obj = RangeFreqQuery2(arr)
print(obj.query(0,0,2))
print(obj.query(0,2,1))
print(obj.query(3,3,2))
print(obj.query(2,2,1))