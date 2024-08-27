from typing import List

'''
示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2

'''


## 从前往后找，一次找到能跳到最后的最靠前的位置，比如先看能一次跳到 4 的最靠前的位置是1 ，然后再考虑从0 跳到1靠最前的位置是那个
def jump(nums: List[int]) -> int:
    position = len(nums) - 1
    step = 0
    while position > 0:
        for i in range(position):
            if (i + nums[i]) >= position:
                position = i
                step += 1
                break
    if position == 0:
        return step


# 从前往后一直跳，尽可能的选择最大的，如果i == 上一次的最大位置，step ++, 这里记录的是起跳的位置，最后的位置是目标，不是起跳的位置，不记录
def jump2(nums: List[int]) -> int:
    max_po = 0
    last_end = 0
    step = 0
    for i in range(len(nums) - 1):
        max_po = max(i + nums[i], max_po)
        if i == last_end:
            last_end = max_po
            step += 1

    return step


print(jump([2, 3, 1, 1, 4]))
print(jump2([2, 1]))
