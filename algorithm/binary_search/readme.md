## 二分查找

### 1. lower_bound 算法：

作用：lower_bound 返回的是第一个不小于（即`大于或等于`）某个值的位置，即在有序序列中，返回第一个不小于给定值的位置。

原理：它通过二分查找，在 O(log n) 的时间复杂度内找到指定的元素或插入位置。

解释：lower_bound 常用于查找大于等于目标值的元素，并且返回的位置通常被用作插入该元素的合适位置以保持有序。

应用：
- 核心要素
- 注意区间开闭，三种都可以
- 循环结束条件：当前区间内没有元素
- 下一次二分查找区间：不能再查找(区间不包含)mid，防止死循环
- 返回值：大于等于target的第一个下标（注意循环不变量）

- 有序数组中二分查找的四种类型（下面的转换仅适用于数组中都是整数）
1. 第一个大于等于x的下标： low_bound(x)
2. 第一个大于x的下标：可以转换为`第一个大于等于 x+1 的下标` ，low_bound(x+1)
3. 最后一个一个小于x的下标：可以转换为`第一个大于等于 x 的下标` 的`左边位置`, low_bound(x) - 1;
4. 最后一个小于等于x的下标：可以转换为`第一个大于等于 x+1 的下标` 的 `左边位置`, low_bound(x+1) - 1;


```python
def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# 测试
arr = [1, 2, 4, 4, 5, 6]
print(lower_bound(arr, 4))  # 输出: 2

```

### 2. upper_bound 算法：

作用：upper_bound 返回的是`第一个大于`某个值的位置，即在有序序列中，找到第一个比给定值大的元素的位置。

原理：与 lower_bound 类似，也是通过二分查找来找到目标值在区间中的上界。

解释：upper_bound 用于查找严格大于目标值的元素。通常在查找区间的上界时使用。

```python
def upper_bound(arr, target):
    left, right = 0, len(arr) -1 
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# 测试
arr = [1, 2, 4, 4, 5, 6]
print(upper_bound(arr, 4))  # 输出: 4

```
