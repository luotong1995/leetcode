from typing import List


#
# def threeSum(nums: List[int]) -> List[List[int]]:
#     n = len(nums)
#     ans = []
#     indexs = set()
#     for i in range(n):
#         for j in range(i + 1, n):
#             for z in range(j + 1, n):
#                 if i != j and j != z and i != z and (nums[i] + nums[j] + nums[z] == 0):
#                     temp = [nums[i], nums[j], nums[z]]
#                     temp.sort()
#                     temp = ','.join([str(a) for a in temp])
#                     if temp not in indexs:
#                         indexs.add(temp)
#                         ans.append([nums[i], nums[j], nums[z]])
#
#     return ans


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = []
    indexs = set()
    for i in range(n):
        if nums[i] > 0:
            return ans
        if i > 0 and nums[i] == nums[i - 1]:  # x上一个数和x相等，不再做重复动作，直接跳过
            continue
        j = i + 1
        z = n - 1
        while j < z:
            v = nums[i] + nums[j] + nums[z]
            if v < 0:
                j += 1
            elif v > 0:
                z -= 1
            else:
                temp = [nums[i], nums[j], nums[z]]
                temp.sort()
                temp = ','.join([str(a) for a in temp])
                if temp not in indexs:
                    indexs.add(temp)
                    ans.append([nums[i], nums[j], nums[z]])
                j += 1

                while j < z and nums[j] == nums[j - 1]:  # 跳过重复数字
                    j += 1

                z -= 1
                while z > j and nums[z] == nums[z + 1]:
                    z -= 1
    return ans


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
