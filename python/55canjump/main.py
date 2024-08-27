from typing import List


# 从前往后跳跃，从最开始往后遍历，当index 大于当前能到达的最远的地方reach，表示不能正常的到达终点
def canJump2(nums: List[int]) -> bool:
    reach = 0
    for i in range(len(nums)):
        if i > reach:
            return False
        reach = max(reach, i + nums[i])
    return True


# 从后往前推，一次判断当前的位置能否正常跳跃到最后的位置，如果最后i = 0
def canJump3(nums: List[int]) -> bool:
    last_index = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= last_index:
            last_index = i
    return last_index == 0


def canJump(nums: List[int]) -> bool:
    if len(nums) < 2:
        return True
    if 0 not in nums:
        return True
    index_l = []
    for i in range(len(nums)):
        if nums[i] == 0:
            index_l.append(i)
    for item in index_l:
        if item == 0:
            return False
        a = nums[:item]
        res = []
        for i in range(len(a)):
            if item != len(nums) - 1:
                b = a[i] <= item - i
            else:
                b = False
            res.append(b)
        if all(res):
            return False
    return True


print(canJump([2, 0, 0]))
