'''
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。


输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。



输入: nums = [2,3,0,1,4]
输出: 2
'''
from typing import List


# 从后往前找，直到找到最最前面的位置
def jump(nums: List[int]) -> int:
    position = len(nums) - 1
    step = 0
    while position > 0:
        for i in range(position):
            if i + nums[i] >= position:
                position = i
                step += 1
                break
    return step



if __name__ == '__main__':
    print(jump([2, 3, 0, 1, 4]))
    print(jump([4, 3, 1, 1, 4]))
