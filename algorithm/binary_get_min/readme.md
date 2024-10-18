### 二分查找求最小值
假设我们在一个升序数组中，寻找满足某个条件的最小值。下面的示例是寻找数组中`第一个大于等于`目标值的元素。

```python
def binary_search_min(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:  # 尝试找到更小的位置，向左找更小的位置
            right = mid - 1  # 收缩右边界
        else:
            left = mid + 1  # 增大左边界

    return left

# 测试
nums = [1, 3, 5, 7, 9]
print(binary_search_min(nums, 6))  # 输出: 3 (元素 7 的位置)

```


### 二分查找求最大值
假设我们在一个升序数组中，寻找满足某个条件的最大值。下面的示例是寻找数组中`最后一个小于等于`目标值的元素。

```python
def binary_search_max(nums, target):
    left, right = 0, len(nums) - 1
    result = -1  # 如果没有找到，返回 -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:  # 尝试找到更大的位置，尝试向右找更大的解
            left = mid + 1  # 增大左边界
        else: #nums[mid] > target，缩小范围
            right = mid - 1  # 收缩右边界

    return right

# 测试
nums = [1, 3, 5, 7, 9]
print(binary_search_max(nums, 6))  # 输出: 2 (元素 5 的位置)


```