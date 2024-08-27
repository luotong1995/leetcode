from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    max_res = 0
    res = 0
    count_zero = 0
    sub_list = []
    for item in nums:
        if item == 1:
            res += 1
            max_res = max(max_res, res)
            sub_list.append(item)
        else:
            if k > 0:
                if count_zero < k:
                    sub_list.append(item)
                    count_zero += 1
                    res += 1
                else:
                    while sub_list.pop(0) == 1:
                        res -= 1
                    sub_list.append(item)
                max_res = max(max_res, res)
            else:
                while len(sub_list) > 0:
                    if sub_list.pop(0):
                        res -= 1
    return max_res


# 窗口长度单调变长
def longestOnes2(nums: List[int], k: int) -> int:
    l = 0
    r = 0
    while r < len(nums):
        if nums[r] == 0:
            k -= 1
        r += 1
        if k < 0:
            if nums[l] == 0:
                k += 1
            l += 1

    return r - l



# print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=0))
print(longestOnes2([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=0))
# print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
